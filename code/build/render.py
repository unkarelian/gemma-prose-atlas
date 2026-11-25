"""Render the static site (site/) from results/atlas.json and live/findings.json.   python3 build/render.py"""
import html, json, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); SITE = os.environ.get("PI_SITE") or os.path.join(ROOT, "site"); PUBLIC = bool(os.environ.get("PI_PUBLIC"))
TITLE = "Gemma prose interpretability"; NAV = [("index.html", "Overview"), ("findings.html", "Findings"), ("atlas.html", "Prose atlas")]
esc = html.escape
def shell(fname, title, body, head="", scripts="", main_class="wrap"):
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h == fname else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="assets/site.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">{head}
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap"><a class="brand" href="index.html">{TITLE}<small>Gemma 3 4B-it · Gemma Scope 2</small></a>
<nav class="site-nav" aria-label="Site">{nav}</nav></div></header>
<main id="main" class="{main_class}">{body}</main>
<footer class="site-foot"><div class="wrap"><span>Interpretability research on prose in Gemma 3 4B-it. Feature labels are best guesses. One model.</span><span>Built {time.strftime('%Y-%m-%d')}</span></div></footer>
{scripts}</body></html>"""
def write(name, s): open(os.path.join(SITE, name), "w", encoding="utf-8").write(s); print("wrote", name, f"{len(s.encode()) // 1024} KB")
js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
F = json.load(open(os.environ.get("PI_FINDINGS") or os.path.join(ROOT, "live", "findings.json")))
# ------------------------------------------------------------ findings (generated from the running list)
CSS = """<style>.fg{margin:28px 0}.fg h2{margin:0 0 10px}.fc{margin:12px 0;padding:16px 20px}.fc h3{margin:0 0 .4em;font-size:18px}.fc p{margin:.4em 0;max-width:var(--prose)}
.tiles{display:flex;gap:12px;flex-wrap:wrap;margin:10px 0}.tile{border:1px solid var(--border);border-radius:10px;padding:8px 14px}.tile b{display:block;font-size:22px;color:var(--accent)}.tile span{font-size:13px;color:var(--muted)}
.bars{margin:10px 0}.bar{display:grid;grid-template-columns:minmax(160px,42%) 1fr auto;gap:10px;align-items:center;font-size:14px;margin:4px 0}.bar .tr{height:10px;background:var(--plane);border-radius:5px;overflow:hidden}.bar .tr i{display:block;height:100%;background:var(--accent)}
.bar .n{font-variant-numeric:tabular-nums}.bar small{color:var(--muted);margin-left:6px}.hero{padding:48px 0 12px;max-width:900px}.hero h1{font-size:clamp(30px,4.2vw,50px);margin:.1em 0 .3em}
.chain{counter-reset:c;list-style:none;padding:0;max-width:var(--prose)}.chain li{counter-increment:c;padding:8px 0 8px 40px;position:relative;border-bottom:1px solid var(--border)}.chain li::before{content:counter(c);position:absolute;left:0;top:8px;width:26px;height:26px;border-radius:50%;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:13px;font-weight:650}
.chain small{display:block;color:var(--text-2)}</style>"""
def card(f):
    s = f'<article class="card fc" id="{esc(f["id"])}"><h3>{esc(f["title"])}</h3><p>{f["body"]}</p>'
    if f.get("stats"): s += '<div class="tiles">' + "".join(f'<div class="tile"><b>{esc(str(x["value"]))}</b><span>{esc(x["label"])}</span></div>' for x in f["stats"]) + "</div>"
    if f.get("bars"): s += '<div class="bars">' + "".join(f'<div class="bar"><span>{esc(b["label"])}</span><span class="tr"><i style="width:{100 * b["value"] / b["max"]:.1f}%"></i></span><span class="n">{b["value"]}{"<small>" + esc(b["note"]) + "</small>" if b.get("note") else ""}</span></div>' for b in f["bars"]) + "</div>"
    return s + "</article>"
groups = []
for f in F["findings"]:
    if f["link"] not in groups: groups.append(f["link"])
body = '<div class="page-head"><p class="kicker">Findings</p><h1>What has been found so far</h1><p class="lede">Each card is one result with its numbers. The list grows as experiments finish.</p></div>'
for g in groups: body += f'<section class="fg"><h2>{esc(g)}</h2>' + "".join(card(f) for f in F["findings"] if f["link"] == g) + "</section>"
write("findings.html", shell("findings.html", f"Findings · {TITLE}", body, head=CSS))
CHAIN = [("Is an AI more likely to cooperate with another AI agent?", "Refusal and instruction-following under human-style and agent-style wording."),
         ("How does an AI know when it is talking to an AI?", "A shared “written by an LLM” direction in the residual stream, tested on prose and on requests."),
         ("Why does AI rate AI prose so highly?", "Gemma judging matched human and LLM versions of the same brief, against its own surprisal and the authorship direction."),
         ("Is AI prose used for that distinction?", "Whether the direction learned from fiction transfers to requests, and whether steering it changes judgments."),
         ("More cooperative, or are agents simply more persistent?", "Second-turn pushes in human and agent wording after a refusal."),
         ("Are LLM-phrased requests followed better or refused less?", "The same asks under eleven wrappers that vary wording and stated sender."),
         ("Does an AI see another agent as similar to itself?", "Whether text attributed to another AI sits closer to “mine” than to “a human's”.")]
CHAIN_HTML = "" if PUBLIC else '<section><h2>The chain of questions</h2><ol class="chain">' + "".join(f"<li>{esc(q)}<small>{esc(a)}</small></li>" for q, a in CHAIN) + "</ol></section>"
HEAD_IDS = ("rain", "rain_causal", "base_prose", "surgery", "detector", "mech_heads", "tgwa") if PUBLIC else ("rain", "rain_causal", "surprisal", "dirs", "names", "judge", "comply")
LEDE = "Gemma writes the same briefs as humans and other models. Every text is read back through the model with 34 layers of transcoders. The atlas maps the features involved; the findings cover where its prose habits come from, why it prefers its own style, how it tells human from AI writing, and two ways of editing the habits out." if PUBLIC else "Gemma writes the same briefs as humans and other models. Every text is read back through the model with 34 layers of transcoders. The atlas maps the features involved; the findings follow a chain of questions about AI talking to AI."
idx = f"""<section class="hero"><p class="kicker">Gemma 3 4B-it · Gemma Scope 2 transcoders</p><h1>How Gemma writes prose, and how it knows who wrote a text</h1>
<p class="lede">{LEDE}</p>
<p><a class="btn" href="atlas.html">Open the prose atlas</a> <a class="btn" href="findings.html">Read the findings</a></p></section>
{CHAIN_HTML}
<section class="fg"><h2>Headline results</h2>{''.join(card(f) for f in F['findings'] if f['id'] in HEAD_IDS)}</section>"""
write("index.html", shell("index.html", TITLE, idx, head=CSS))
# ------------------------------------------------------------ atlas
A = json.load(open(os.environ.get("PI_ATLAS") or os.path.join(ROOT, "results", "atlas.json")))
ACSS = """<style>
.ah{padding:28px 0 6px}.ah h1{margin:.1em 0 .2em}.abar{position:sticky;top:57px;z-index:20;background:var(--bg);display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:10px 0;border-bottom:1px solid var(--border);margin-bottom:16px}
.tabs{display:flex;gap:6px;flex-wrap:wrap}.tabs button,.pill{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:999px;padding:6px 14px;font:inherit;font-size:14.5px;cursor:pointer}
.tabs button[aria-selected=true],.pill.on{background:var(--text);color:var(--bg);border-color:var(--text)}.abar input{margin-left:auto;width:min(340px,100%);padding:8px 12px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit}
.cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;align-items:start}.cg h3{margin:0;font-size:16px}.cg .meta{font-size:13px;color:var(--muted);margin:2px 0 8px}
.strip{display:grid;grid-template-columns:repeat(34,1fr);gap:1px;margin:6px 0 10px}.strip i{height:12px;border-radius:2px;background:var(--plane)}
.frow{display:flex;gap:8px;align-items:baseline;padding:5px 6px;border-radius:6px;cursor:pointer;font-size:14px;width:100%;text-align:left;border:0;background:none;color:var(--text);font-family:inherit}.frow:hover{background:var(--plane)}
.frow .k{font-family:var(--mono);font-size:12.5px;color:var(--muted);min-width:78px}.frow .l{flex:1}.frow .d{font-size:12px;color:var(--muted);white-space:nowrap;font-variant-numeric:tabular-nums}
.more{font-size:13.5px;background:none;border:0;color:var(--accent);cursor:pointer;padding:4px 6px;font-family:inherit}.pills{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}@media(max-width:900px){.two{grid-template-columns:1fr}}
table.lm{border-collapse:separate;border-spacing:2px;font-size:12px}table.lm th{font-weight:500;color:var(--muted);padding:0 2px}table.lm th.g{text-align:right;white-space:nowrap;padding-right:8px;color:var(--text-2);font-size:13px}table.lm td{width:20px;height:20px;border-radius:3px;text-align:center;font-size:10.5px;color:var(--bg)}
#dr{position:fixed;top:0;right:0;bottom:0;width:min(640px,100vw);background:var(--surface);border-left:1px solid var(--border);box-shadow:var(--shadow);z-index:50;overflow:auto;padding:22px 24px;transform:translateX(105%);transition:transform .18s}#dr.open{transform:none}
#dr h2{margin:.2em 0 .1em;font-size:21px}#dr .x{position:absolute;top:12px;right:14px;border:0;background:none;font-size:24px;cursor:pointer;color:var(--muted)}#dr h4{margin:1.3em 0 .4em;font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.rb{display:grid;grid-template-columns:130px 1fr 52px;gap:8px;align-items:center;font-size:13px;margin:2px 0}.rb .tr{height:9px;background:var(--plane);border-radius:5px;overflow:hidden}.rb .tr i{display:block;height:100%}.rb .n{text-align:right;font-variant-numeric:tabular-nums;color:var(--text-2)}
.tok{display:inline-block;font-family:var(--mono);font-size:12.5px;background:var(--plane);border-radius:5px;padding:1px 6px;margin:2px 3px 2px 0;white-space:pre}.exm{font-size:14px;margin:6px 0;padding:6px 10px;border-left:3px solid var(--border);color:var(--text-2)}.exm mark{background:var(--accent-soft);color:var(--text);font-weight:650;padding:0 2px;border-radius:3px}.exm .w{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-right:6px}
.conf{font-size:11.5px;color:var(--muted)}.conf.high{color:var(--green)}.conf.low{color:var(--amber)}</style>"""
AJS = """<script>const A=__DATA__;
const $=s=>document.querySelector(s),E=s=>(s+'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const BY={};A.features.forEach(f=>BY[f.key]=f);let tab='groups',q='',sel=null;
const CN={'wp/human':'human (stories)','wp/gemma':'Gemma (stories)','wp/claude':'Claude','wp/glm':'GLM','books/human':'authors (novels)','books/gemma':'Gemma (novels)','books/haiku':'Haiku','books/gpt':'GPT','books/glm':'GLM (novels)','wp/gemma_plain':'Gemma, plain','wp/gemma_lit':'Gemma, literary','wp/gemma_greedy':'Gemma, greedy','wp/gemma_raw':'Gemma, raw text','wp/human_raw':'human, raw text','taste/approved':'approved edit','taste/rejected':'rejected draft'};
const CC=c=>c.includes('human')||c.includes('approved')?'var(--pole0)':c.includes('gemma')||c.includes('rejected')?'var(--pole1)':'var(--mid)';
const KN={wp_gemma_vs_human:'Gemma vs human (stories)',books_gemma_vs_human:'Gemma vs authors (novels)',wp_llm_vs_human:'other LLMs vs human (stories)',books_llm_vs_human:'other LLMs vs authors (novels)',wp_gemma_vs_llm:'Gemma vs other LLMs (stories)',books_gemma_vs_llm:'Gemma vs other LLMs (novels)',lit_vs_plain:'literary vs plain instruction',lit_vs_default:'literary instruction vs default',plain_vs_default:'plain instruction vs default',greedy_vs_sampled:'greedy vs sampled',raw_gemma_vs_human:'Gemma vs human, raw text',chat_vs_raw_gemma:'chat template vs raw text',taste_rejected_vs_approved:'rejected draft vs approved edit'};
function match(f){if(!q)return true;const s=(f.key+' '+f.label+' '+f.note+' '+f.group+' '+f.kind+' '+f.why.join(' ')+' '+f.top.join(' ')).toLowerCase();return q.split(/\\s+/).every(w=>s.includes(w))}
function row(f,extra){return `<button class="frow" data-k="${f.key}"><span class="k">${f.key}</span><span class="l">${E(f.label)}</span>${extra?`<span class="d">${extra}</span>`:''}<span class="conf ${f.conf}">${f.conf}</span></button>`}
function strip(fs){const c=Array(34).fill(0);fs.forEach(f=>c[f.layer]++);const m=Math.max(1,...c);return '<div class="strip" title="layers 0 to 33">'+c.map(n=>`<i style="${n?`background:var(--accent);opacity:${.25+.75*n/m}`:''}"></i>`).join('')+'</div>'}
function vGroups(){const fs=A.features.filter(match);return '<div class="cgrid">'+A.groups.map(g=>{const x=fs.filter(f=>f.group==g);if(!x.length)return '';const show=x.slice(0,8);
 return `<div class="card cg"><h3>${E(g)}</h3><div class="meta">${x.length} features</div>${strip(x)}${show.map(f=>row(f)).join('')}${x.length>8?`<div class="rest" hidden>${x.slice(8).map(f=>row(f)).join('')}</div><button class="more">Show all ${x.length}</button>`:''}</div>`}).join('')+'</div>'}
let curC=Object.keys(A.contrasts)[0];
function vContrasts(){const ks=Object.keys(A.contrasts);const fs=A.features.filter(match).map(f=>[f,f.contrasts.find(c=>c.c==curC)]).filter(x=>x[1]);
 const pos=fs.filter(x=>x[1].d0>0).sort((a,b)=>Math.min(b[1].d0,b[1].d1)-Math.min(a[1].d0,a[1].d1)),neg=fs.filter(x=>x[1].d0<0).sort((a,b)=>Math.max(a[1].d0,a[1].d1)-Math.max(b[1].d0,b[1].d1));const [a,b]=(KN[curC]||curC).split(' vs ');
 const m=A.contrasts[curC];return `<div class="pills">${ks.map(k=>`<button class="pill ${k==curC?'on':''}" data-c="${k}">${E(KN[k]||k)}</button>`).join('')}</div><p class="muted">Paired by brief: ${m.n[0]} + ${m.n[1]} briefs in the two halves; effect sizes on the two halves correlate ${m.half_corr} across all features. Numbers are the paired effect size on each half and the change in firing rate.</p>
 <div class="two"><div class="card"><h3>Fires more for ${E(a)}</h3>${pos.map(x=>row(x[0],`${x[1].d0} / ${x[1].d1} · ${(100*x[1].dfrac).toFixed(1)} pts`)).join('')||'<p class="muted">none</p>'}</div><div class="card"><h3>Fires more for ${E(b||'the other side')}</h3>${neg.map(x=>row(x[0],`${x[1].d0} / ${x[1].d1} · ${(100*x[1].dfrac).toFixed(1)} pts`)).join('')||'<p class="muted">none</p>'}</div></div>`}
function vTags(){const ts=Object.entries(A.tags);const one=([t,v])=>{const fs=v.feats.map(k=>BY[k]).filter(f=>f&&match(f));if(!fs.length)return '';const pc=v.per_class;
 return `<div class="card cg"><h3>${E(t.replace('pre:','before: ').replace(/_/g,' '))}</h3><div class="meta">${(v.n[0]+v.n[1]).toLocaleString()} tokens · human ${pc[0].toLocaleString()}, Gemma ${pc[1].toLocaleString()}, other LLM ${pc[2].toLocaleString()}</div>${strip(fs)}${fs.map(f=>row(f)).join('')}</div>`};
 return `<p class="muted">Features that fire on the tokens of a construction, and (“before:”) on the token just before it starts, where the model decides to begin it. Token counts are within the first 640 tokens of each document.</p><h3>On the construction</h3><div class="cgrid">${ts.filter(x=>!x[0].startsWith('pre:')).map(one).join('')}</div><h3 style="margin-top:28px">One token before</h3><div class="cgrid">${ts.filter(x=>x[0].startsWith('pre:')).map(one).join('')}</div>`}
function vMap(){const fs=A.features.filter(match);let h='<div class="card" style="overflow:auto"><table class="lm"><tr><th></th>'+[...Array(34).keys()].map(l=>`<th>${l}</th>`).join('')+'</tr>';
 A.groups.forEach(g=>{const c=Array(34).fill(0);fs.filter(f=>f.group==g).forEach(f=>c[f.layer]++);const m=Math.max(1,...c);h+=`<tr><th class="g">${E(g)}</th>`+c.map(n=>`<td style="${n?`background:var(--accent);opacity:${.3+.7*n/m}`:'background:var(--plane)'}">${n||''}</td>`).join('')+'</tr>'});return h+'</table></div><p class="muted">Number of atlas features per group and layer.</p>'}
function vAll(){return '<div class="card">'+A.features.filter(match).map(f=>row(f,E(f.group))).join('')+'</div>'}
function render(){const v={groups:vGroups,contrasts:vContrasts,tags:vTags,map:vMap,all:vAll}[tab]();$('#view').innerHTML=v;document.querySelectorAll('.tabs button').forEach(b=>b.setAttribute('aria-selected',b.dataset.t==tab))}
function open_(k){const f=BY[k];if(!f)return;sel=k;history.replaceState(null,'','#'+k);const mx=Math.max(.001,...Object.values(f.rates));
 let h=`<button class="x" aria-label="Close">×</button><div class="k muted" style="font-family:var(--mono)">${f.key} · layer ${f.layer} · ${E(f.kind)} · <span class="conf ${f.conf}">${f.conf} confidence</span></div><h2>${E(f.label)}</h2><p class="chip">${E(f.group)}</p><p>${E(f.note)}</p>`;
 h+='<h4>Share of tokens it fires on, by writer</h4>'+Object.entries(f.rates).map(([c,v])=>`<div class="rb"><span>${E(CN[c]||c)}</span><span class="tr"><i style="width:${100*v/mx}%;background:${CC(c)}"></i></span><span class="n">${(100*v).toFixed(1)}%</span></div>`).join('');
 if(f.contrasts.length)h+='<h4>Writer contrasts (effect size on each half)</h4>'+f.contrasts.map(c=>`<div class="rb" style="grid-template-columns:1fr auto"><span>${E(KN[c.c]||c.c)}</span><span class="n" style="width:auto">${c.d0} / ${c.d1} · ${(100*c.dfrac).toFixed(1)} pts</span></div>`).join('');
 const tg=f.why.filter(w=>w.startsWith('tag:'));if(tg.length)h+='<h4>Constructions</h4>'+tg.map(w=>`<span class="tok">${E(w.slice(4).replace('pre:','before: '))}</span>`).join('');
 if(f.attract.length)h+='<h4>Decision points it writes toward</h4>'+f.attract.map(a=>`<div class="rb" style="grid-template-columns:1fr auto"><span>${E(a.set)}: “${E(a.target)}”</span><span class="n" style="width:auto">rank ${a.rank}</span></div>`).join('');
 if(f.entropy)h+=`<h4>Relation to the model's own uncertainty</h4><p class="muted">Correlation of firing with next-token entropy: ${f.entropy.all.r_entropy}. Firing rate by entropy quartile (low to high), human text: ${f.entropy.human.fires_by_entropy_quartile.join(', ')}; Gemma's text: ${f.entropy.gemma.fires_by_entropy_quartile.join(', ')}.</p>`;
 h+='<h4>Output: tokens it promotes</h4>'+f.top.map(t=>`<span class="tok">${E(t)}</span>`).join('')+'<h4>Tokens it suppresses</h4>'+f.bottom.map(t=>`<span class="tok">${E(t)}</span>`).join('');
 h+='<h4>Strongest examples (firing token marked)</h4>'+(f.ex.map(x=>`<div class="exm"><span class="w">${E(x.w)}</span>${E(x.t).replace('[[','<mark>').replace(']]','</mark>')}</div>`).join('')||'<p class="muted">Examples withheld (published novels or private text).</p>');
 $('#dr').innerHTML=h;$('#dr').classList.add('open')}
document.addEventListener('click',e=>{const r=e.target.closest('.frow');if(r)return open_(r.dataset.k);if(e.target.closest('#dr .x')){$('#dr').classList.remove('open');history.replaceState(null,'',' ');return}
 const t=e.target.closest('.tabs button');if(t){tab=t.dataset.t;return render()}const p=e.target.closest('.pill');if(p){curC=p.dataset.c;return render()}
 const m=e.target.closest('.more');if(m){m.previousElementSibling.hidden=false;m.remove()}});
document.addEventListener('keydown',e=>{if(e.key=='Escape')$('#dr').classList.remove('open')});
$('#q').addEventListener('input',e=>{q=e.target.value.toLowerCase().trim();render()});render();if(location.hash.length>1)open_(decodeURIComponent(location.hash.slice(1)));
</script>"""
nlab = sum(1 for f in A["features"] if f["label"] != "(unlabelled)")
abody = f"""<div class="ah"><p class="kicker">Prose atlas</p><h1>{len(A['features'])} transcoder features involved in prose</h1>
<p class="lede">Chosen from 557,056 features (34 layers × 16,384) because they fire differently for different writers of the same brief, attach to a construction, or write toward one of Gemma's habitual tokens. {nlab} are labelled. Click a feature for its firing rates by writer, output tokens and examples. Link to one with <span class="mono">atlas.html#L26.1900</span>.</p></div>
<div class="abar"><div class="tabs" role="tablist"><button data-t="groups">By theme</button><button data-t="contrasts">By writer contrast</button><button data-t="tags">By construction</button><button data-t="map">Layer map</button><button data-t="all">All</button></div><input id="q" type="search" placeholder="Search labels, notes, tokens, ids" aria-label="Search features"></div>
<div id="view"></div><aside id="dr" aria-label="Feature detail"></aside>"""
write("atlas.html", shell("atlas.html", f"Prose atlas · {TITLE}", abody, head=ACSS, scripts=AJS.replace("__DATA__", js(A))))
