<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Functions — Complete Reference</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0d0d0d;
    --surface: #141414;
    --surface2: #1c1c1c;
    --border: rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.12);
    --accent: #b3ff5c;
    --accent2: #5cf4ff;
    --accent3: #ff6b6b;
    --text: #f0f0f0;
    --muted: #888;
    --muted2: #555;
    --code-bg: #111;
    --keyword: #ff79c6;
    --func: #b3ff5c;
    --string: #f1fa8c;
    --comment: #6272a4;
    --builtin: #8be9fd;
    --num: #bd93f9;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    font-size: 16px;
    line-height: 1.7;
  }

  /* HEADER */
  header {
    padding: 80px 0 60px;
    border-bottom: 1px solid var(--border2);
    position: relative;
    overflow: hidden;
  }
  header::before {
    content: '';
    position: absolute;
    top: -80px; left: -80px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(179,255,92,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  header::after {
    content: 'def';
    position: absolute;
    right: 60px; bottom: -30px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 160px;
    font-weight: 700;
    color: rgba(255,255,255,0.02);
    letter-spacing: -4px;
    pointer-events: none;
  }
  .container { max-width: 860px; margin: 0 auto; padding: 0 40px; }

  .tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    background: rgba(179,255,92,0.08);
    border: 1px solid rgba(179,255,92,0.2);
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 20px;
    letter-spacing: 0.1em;
  }

  h1 {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -1.5px;
    margin-bottom: 16px;
  }
  h1 span { color: var(--accent); }

  .subtitle {
    font-size: 16px;
    color: var(--muted);
    max-width: 500px;
    font-weight: 400;
  }

  .meta-row {
    display: flex;
    gap: 24px;
    margin-top: 32px;
    flex-wrap: wrap;
  }
  .meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }
  .meta-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
  }

  /* TOC */
  .toc {
    background: var(--surface);
    border: 1px solid var(--border2);
    border-left: 3px solid var(--accent);
    border-radius: 8px;
    padding: 28px 32px;
    margin: 48px 0;
  }
  .toc-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .toc ol {
    padding-left: 20px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 32px;
  }
  .toc li { font-size: 14px; }
  .toc a { color: var(--muted); text-decoration: none; transition: color 0.2s; }
  .toc a:hover { color: var(--accent); }

  /* SECTIONS */
  section { padding: 56px 0; border-bottom: 1px solid var(--border); }
  section:last-of-type { border-bottom: none; }

  .section-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted2);
    letter-spacing: 0.1em;
    margin-bottom: 6px;
  }

  h2 {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 20px;
    color: var(--text);
  }
  h2 .hl { color: var(--accent); }

  h3 {
    font-size: 16px;
    font-weight: 600;
    color: var(--text);
    margin: 28px 0 10px;
    letter-spacing: -0.2px;
  }

  p { color: rgba(240,240,240,0.8); margin-bottom: 16px; font-size: 15px; }

  /* CODE BLOCKS */
  .code-wrap {
    background: var(--code-bg);
    border: 1px solid var(--border2);
    border-radius: 8px;
    overflow: hidden;
    margin: 20px 0;
  }
  .code-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    background: rgba(255,255,255,0.03);
    border-bottom: 1px solid var(--border);
  }
  .code-lang {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted2);
    letter-spacing: 0.08em;
  }
  .code-dots { display: flex; gap: 6px; }
  .code-dots span {
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--border2);
  }
  pre {
    padding: 20px 24px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.8;
  }

  /* syntax highlighting via spans */
  .kw { color: var(--keyword); }
  .fn { color: var(--func); }
  .st { color: var(--string); }
  .cm { color: var(--comment); font-style: italic; }
  .bi { color: var(--builtin); }
  .nm { color: var(--num); }
  .px { color: var(--accent2); }

  /* CALLOUT BOXES */
  .callout {
    border-radius: 8px;
    padding: 18px 22px;
    margin: 20px 0;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    font-size: 14px;
  }
  .callout-icon {
    font-size: 16px;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .callout-text { line-height: 1.6; }
  .callout.tip {
    background: rgba(179,255,92,0.06);
    border: 1px solid rgba(179,255,92,0.15);
    color: rgba(179,255,92,0.9);
  }
  .callout.warn {
    background: rgba(255,107,107,0.06);
    border: 1px solid rgba(255,107,107,0.15);
    color: rgba(255,150,150,0.9);
  }
  .callout.info {
    background: rgba(92,244,255,0.06);
    border: 1px solid rgba(92,244,255,0.15);
    color: rgba(92,244,255,0.9);
  }

  /* INLINE CODE */
  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    background: rgba(255,255,255,0.06);
    border: 1px solid var(--border2);
    padding: 2px 7px;
    border-radius: 4px;
    color: var(--accent2);
  }

  /* TABLE */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
  }
  .data-table th {
    background: rgba(255,255,255,0.04);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 0.1em;
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border2);
    font-weight: 500;
  }
  .data-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    color: rgba(240,240,240,0.75);
    vertical-align: top;
  }
  .data-table tr:last-child td { border-bottom: none; }
  .data-table tr:hover td { background: rgba(255,255,255,0.02); }

  /* ANATOMY DIAGRAM */
  .anatomy {
    background: var(--surface);
    border: 1px solid var(--border2);
    border-radius: 8px;
    padding: 28px;
    margin: 20px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    line-height: 2.2;
  }
  .anatomy .arrow-label {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    color: var(--muted);
  }
  .anatomy .highlight-box {
    display: inline-block;
    border-bottom: 2px solid;
    position: relative;
  }

  /* BADGE */
  .badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 500;
  }
  .badge-green { background: rgba(179,255,92,0.12); color: var(--accent); border: 1px solid rgba(179,255,92,0.2); }
  .badge-blue { background: rgba(92,244,255,0.1); color: var(--accent2); border: 1px solid rgba(92,244,255,0.2); }
  .badge-red { background: rgba(255,107,107,0.1); color: var(--accent3); border: 1px solid rgba(255,107,107,0.2); }

  /* FOOTER */
  footer {
    padding: 40px;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--muted2);
    border-top: 1px solid var(--border);
  }
  footer span { color: var(--accent); }
</style>
</head>
<body>

<header>
  <div class="container">
    <div class="tag">📄 README.md</div>
    <h1>Python <span>Functions</span><br>Complete Reference</h1>
    <p class="subtitle">Everything you need to know about defining, calling, and mastering functions in Python — from basics to advanced patterns.</p>
    <div class="meta-row">
      <div class="meta-item"><span class="meta-dot"></span> Python 3.10+</div>
      <div class="meta-item"><span class="meta-dot"></span> Beginner to Advanced</div>
      <div class="meta-item"><span class="meta-dot"></span> 10 Topics Covered</div>
      <div class="meta-item"><span class="meta-dot"></span> 30+ Code Examples</div>
    </div>
  </div>
</header>

<div class="container">

  <!-- TABLE OF CONTENTS -->
  <div class="toc">
    <div class="toc-title">// Table of Contents</div>
    <ol>
      <li><a href="#basics">What is a Function?</a></li>
      <li><a href="#anatomy">Anatomy of a Function</a></li>
      <li><a href="#params">Parameters &amp; Arguments</a></li>
      <li><a href="#return">Return Values</a></li>
      <li><a href="#scope">Scope &amp; Namespaces</a></li>
      <li><a href="#lambda">Lambda Functions</a></li>
      <li><a href="#decorators">Decorators</a></li>
      <li><a href="#generators">Generators</a></li>
      <li><a href="#advanced">Advanced Patterns</a></li>
      <li><a href="#best">Best Practices</a></li>
    </ol>
  </div>

  <!-- 1. BASICS -->
  <section id="basics">
    <div class="section-num">01 —</div>
    <h2>What is a <span class="hl">Function?</span></h2>
    <p>A function is a reusable, named block of code that performs a specific task. You define it once, call it as many times as you need. Functions are the backbone of writing clean, maintainable Python.</p>
    <p>They help you avoid repetition (the DRY principle — Don't Repeat Yourself), make code easier to test, and break big problems into small, manageable pieces.</p>

    <div class="code-wrap">
      <div class="code-header">
        <div class="code-dots"><span></span><span></span><span></span></div>
        <div class="code-lang">python</div>
      </div>
      <pre><span class="cm"># Without a function — repetitive and hard to maintain</span>
<span class="bi">print</span>(<span class="st">"Hello, Alice!"</span>)
<span class="bi">print</span>(<span class="st">"Hello, Bob!"</span>)
<span class="bi">print</span>(<span class="st">"Hello, Charlie!"</span>)

<span class="cm"># With a function — clean, reusable, easy to change</span>
<span class="kw">def</span> <span class="fn">greet</span>(name):
    <span class="bi">print</span>(<span class="st">f"Hello, </span><span class="px">{name}</span><span class="st">!"</span>)

greet(<span class="st">"Alice"</span>)
greet(<span class="st">"Bob"</span>)
greet(<span class="st">"Charlie"</span>)</pre>
    </div>
  </section>

  <!-- 2. ANATOMY -->
  <section id="anatomy">
    <div class="section-num">02 —</div>
    <h2>Anatomy of a <span class="hl">Function</span></h2>
    <p>Every function in Python follows this structure. Understanding each part is key before going deeper.</p>

    <div class="code-wrap">
      <div class="code-header">
        <div class="code-dots"><span></span><span></span><span></span></div>
        <div class="code-lang">python — full anatomy</div>
      </div>
      <pre><span class="kw">def</span> <span class="fn">add_numbers</span>(a: <span class="bi">int</span>, b: <span class="bi">int</span>) -> <span class="bi">int</span>:
    <span class="st">"""
    Adds two integers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: Sum of a and b.
    """</span>
    result = a + b
    <span class="kw">return</span> result

<span class="cm"># Calling the function</span>
total = add_numbers(<span class="nm">10</span>, <span class="nm">20</span>)
<span class="bi">print</span>(total)  <span class="cm"># 30</span></pre>
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>Part</th>
          <th>Syntax</th>
          <th>Purpose</th>
          <th>Required?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Keyword</td>
          <td><code>def</code></td>
          <td>Declares a function definition</td>
          <td><span class="badge badge-red">Required</span></td>
        </tr>
        <tr>
          <td>Name</td>
          <td><code>add_numbers</code></td>
          <td>Identifier used to call the function</td>
          <td><span class="badge badge-red">Required</span></td>
        </tr>
        <tr>
          <td>Parameters</td>
          <td><code>(a, b)</code></td>
          <td>Inputs the function accepts</td>
          <td><span class="badge badge-blue">Optional</span></td>
        </tr>
        <tr>
          <td>Type hints</td>
          <td><code>a: int</code></td>
          <td>Documents expected types (no enforcement)</td>
          <td><span class="badge badge-blue">Optional</span></td>
        </tr>
        <tr>
          <td>Return hint</td>
          <td><code>-> int</code></td>
          <td>Documents what type is returned</td>
          <td><span class="badge badge-blue">Optional</span></td>
        </tr>
        <tr>
          <td>Docstring</td>
          <td><code>"""..."""</code></td>
          <td>Human-readable description</td>
          <td><span class="badge badge-blue">Optional</span></td>
        </tr>
        <tr>
          <td>Body</td>
          <td>indented block</td>
          <td>The actual code that runs</td>
          <td><span class="badge badge-red">Required</span></td>
        </tr>
        <tr>
          <td>Return</td>
          <td><code>return result</code></td>
          <td>Sends a value back to the caller</td>
          <td><span class="badge badge-blue">Optional</span></td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- 3. PARAMETERS -->
  <section id="params">
    <div class="section-num">03 —</div>
    <h2>Parameters <span class="hl">&amp; Arguments</span></h2>
    <p>Python gives you a lot of flexibility in how you pass data into functions. There are five distinct ways.</p>

    <h3>Positional Parameters</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">describe</span>(name, age):
    <span class="bi">print</span>(<span class="st">f"</span><span class="px">{name}</span><span class="st"> is </span><span class="px">{age}</span><span class="st"> years old"</span>)

describe(<span class="st">"Haseeb"</span>, <span class="nm">25</span>)   <span class="cm"># order matters here</span></pre>
    </div>

    <h3>Default Parameter Values</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">power</span>(base, exponent=<span class="nm">2</span>):   <span class="cm"># exponent defaults to 2</span>
    <span class="kw">return</span> base ** exponent

<span class="bi">print</span>(power(<span class="nm">3</span>))       <span class="cm"># 9  — uses default</span>
<span class="bi">print</span>(power(<span class="nm">3</span>, <span class="nm">3</span>))    <span class="cm"># 27 — overrides default</span></pre>
    </div>

    <div class="callout warn">
      <div class="callout-icon">⚠</div>
      <div class="callout-text"><strong>Common gotcha:</strong> Never use mutable objects (lists, dicts) as default parameter values. They are created once at function definition time, not each call. Use <code>None</code> and initialize inside the body instead.</div>
    </div>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python — mutable default bug vs fix</div></div>
      <pre><span class="cm"># BAD — shared across all calls!</span>
<span class="kw">def</span> <span class="fn">add_item_bad</span>(item, items=[]):
    items.append(item)
    <span class="kw">return</span> items

<span class="cm"># GOOD — fresh list each call</span>
<span class="kw">def</span> <span class="fn">add_item_good</span>(item, items=<span class="kw">None</span>):
    <span class="kw">if</span> items <span class="kw">is</span> <span class="kw">None</span>:
        items = []
    items.append(item)
    <span class="kw">return</span> items</pre>
    </div>

    <h3>Keyword Arguments</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">connect</span>(host, port, timeout):
    <span class="bi">print</span>(<span class="st">f"Connecting to </span><span class="px">{host}</span><span class="st">:</span><span class="px">{port}</span><span class="st"> (timeout=</span><span class="px">{timeout}</span><span class="st">s)"</span>)

<span class="cm"># Named — order doesn't matter</span>
connect(timeout=<span class="nm">30</span>, host=<span class="st">"localhost"</span>, port=<span class="nm">5432</span>)</pre>
    </div>

    <h3>*args — Variable Positional Arguments</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">total</span>(*numbers):   <span class="cm"># numbers is a tuple</span>
    <span class="kw">return</span> <span class="bi">sum</span>(numbers)

<span class="bi">print</span>(total(<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>))           <span class="cm"># 6</span>
<span class="bi">print</span>(total(<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>, <span class="nm">40</span>))    <span class="cm"># 100</span></pre>
    </div>

    <h3>**kwargs — Variable Keyword Arguments</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">build_profile</span>(**info):   <span class="cm"># info is a dict</span>
    <span class="kw">for</span> key, value <span class="kw">in</span> info.items():
        <span class="bi">print</span>(<span class="st">f"  </span><span class="px">{key}</span><span class="st">: </span><span class="px">{value}</span><span class="st">"</span>)

build_profile(name=<span class="st">"Haseeb"</span>, role=<span class="st">"dev"</span>, lang=<span class="st">"Python"</span>)</pre>
    </div>

    <div class="callout tip">
      <div class="callout-icon">✦</div>
      <div class="callout-text">The correct order when combining all parameter types: <code>def func(positional, /, normal, *args, keyword_only, **kwargs)</code>. Python enforces this order strictly.</div>
    </div>
  </section>

  <!-- 4. RETURN -->
  <section id="return">
    <div class="section-num">04 —</div>
    <h2>Return <span class="hl">Values</span></h2>
    <p>Functions can return any Python object. If no <code>return</code> statement is present (or just <code>return</code> alone), Python returns <code>None</code>.</p>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="cm"># Return a single value</span>
<span class="kw">def</span> <span class="fn">square</span>(n):
    <span class="kw">return</span> n ** <span class="nm">2</span>

<span class="cm"># Return multiple values (actually a tuple)</span>
<span class="kw">def</span> <span class="fn">min_max</span>(numbers):
    <span class="kw">return</span> <span class="bi">min</span>(numbers), <span class="bi">max</span>(numbers)

low, high = min_max([<span class="nm">3</span>, <span class="nm">1</span>, <span class="nm">9</span>, <span class="nm">4</span>, <span class="nm">7</span>])
<span class="bi">print</span>(low, high)   <span class="cm"># 1 9</span>

<span class="cm"># Early return — guard clause pattern</span>
<span class="kw">def</span> <span class="fn">divide</span>(a, b):
    <span class="kw">if</span> b == <span class="nm">0</span>:
        <span class="kw">return</span> <span class="kw">None</span>   <span class="cm"># early exit</span>
    <span class="kw">return</span> a / b</pre>
    </div>
  </section>

  <!-- 5. SCOPE -->
  <section id="scope">
    <div class="section-num">05 —</div>
    <h2>Scope <span class="hl">&amp; Namespaces</span></h2>
    <p>Python uses the LEGB rule to resolve variable names: <strong>L</strong>ocal → <strong>E</strong>nclosing → <strong>G</strong>lobal → <strong>B</strong>uilt-in.</p>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre>x = <span class="st">"global"</span>

<span class="kw">def</span> <span class="fn">outer</span>():
    x = <span class="st">"enclosing"</span>

    <span class="kw">def</span> <span class="fn">inner</span>():
        x = <span class="st">"local"</span>
        <span class="bi">print</span>(x)   <span class="cm"># local</span>

    inner()
    <span class="bi">print</span>(x)       <span class="cm"># enclosing</span>

outer()
<span class="bi">print</span>(x)           <span class="cm"># global</span>

<span class="cm"># Modifying a global inside a function</span>
counter = <span class="nm">0</span>

<span class="kw">def</span> <span class="fn">increment</span>():
    <span class="kw">global</span> counter
    counter += <span class="nm">1</span>

<span class="cm"># Modifying enclosing scope from nested function</span>
<span class="kw">def</span> <span class="fn">make_counter</span>():
    count = <span class="nm">0</span>
    <span class="kw">def</span> <span class="fn">tick</span>():
        <span class="kw">nonlocal</span> count
        count += <span class="nm">1</span>
        <span class="kw">return</span> count
    <span class="kw">return</span> tick</pre>
    </div>

    <div class="callout info">
      <div class="callout-icon">ℹ</div>
      <div class="callout-text">Avoid <code>global</code> as much as possible. It makes functions harder to test and reason about. Pass values as parameters and return results instead.</div>
    </div>
  </section>

  <!-- 6. LAMBDA -->
  <section id="lambda">
    <div class="section-num">06 —</div>
    <h2>Lambda <span class="hl">Functions</span></h2>
    <p>A lambda is a small, anonymous function defined in a single line. It is limited to a single expression — no statements, no multiple lines. Best used as a short throwaway function passed to another function.</p>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="cm"># Syntax: lambda params: expression</span>
double = <span class="kw">lambda</span> x: x * <span class="nm">2</span>
add    = <span class="kw">lambda</span> a, b: a + b

<span class="cm"># Common use: sorting with a custom key</span>
students = [(<span class="st">"Alice"</span>, <span class="nm">88</span>), (<span class="st">"Bob"</span>, <span class="nm">95</span>), (<span class="st">"Carol"</span>, <span class="nm">72</span>)]

students.sort(<span class="px">key</span>=<span class="kw">lambda</span> s: s[<span class="nm">1</span>], <span class="px">reverse</span>=<span class="kw">True</span>)
<span class="bi">print</span>(students)   <span class="cm"># [('Bob', 95), ('Alice', 88), ('Carol', 72)]</span>

<span class="cm"># With map() and filter()</span>
nums = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>]
squares = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> x: x**<span class="nm">2</span>, nums))
evens   = <span class="bi">list</span>(<span class="bi">filter</span>(<span class="kw">lambda</span> x: x % <span class="nm">2</span> == <span class="nm">0</span>, nums))</pre>
    </div>

    <div class="callout warn">
      <div class="callout-icon">⚠</div>
      <div class="callout-text">If your lambda is getting complex or you need to reuse it, write a proper <code>def</code> function instead. Lambdas are for quick, single-use cases only.</div>
    </div>
  </section>

  <!-- 7. DECORATORS -->
  <section id="decorators">
    <div class="section-num">07 —</div>
    <h2>Decorators</h2>
    <p>A decorator is a function that wraps another function to extend or modify its behavior — without changing the original function's source code. This is one of the most powerful patterns in Python.</p>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python — building a decorator from scratch</div></div>
      <pre><span class="kw">import</span> functools
<span class="kw">import</span> time

<span class="kw">def</span> <span class="fn">timer</span>(func):
    <span class="st">"""Decorator that prints how long a function takes."""</span>
    @functools.wraps(func)   <span class="cm"># preserves original func metadata</span>
    <span class="kw">def</span> <span class="fn">wrapper</span>(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        <span class="bi">print</span>(<span class="st">f"</span><span class="px">{func.__name__}</span><span class="st"> ran in </span><span class="px">{end - start:.4f}</span><span class="st">s"</span>)
        <span class="kw">return</span> result
    <span class="kw">return</span> wrapper

@timer
<span class="kw">def</span> <span class="fn">slow_task</span>():
    time.sleep(<span class="nm">0.5</span>)
    <span class="bi">print</span>(<span class="st">"Task done"</span>)

slow_task()
<span class="cm"># Task done</span>
<span class="cm"># slow_task ran in 0.5002s</span></pre>
    </div>

    <h3>Decorator with Arguments</h3>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">repeat</span>(times):
    <span class="kw">def</span> <span class="fn">decorator</span>(func):
        @functools.wraps(func)
        <span class="kw">def</span> <span class="fn">wrapper</span>(*args, **kwargs):
            <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(times):
                func(*args, **kwargs)
        <span class="kw">return</span> wrapper
    <span class="kw">return</span> decorator

@repeat(<span class="nm">3</span>)
<span class="kw">def</span> <span class="fn">say_hi</span>():
    <span class="bi">print</span>(<span class="st">"Hi!"</span>)

say_hi()   <span class="cm"># prints Hi! three times</span></pre>
    </div>
  </section>

  <!-- 8. GENERATORS -->
  <section id="generators">
    <div class="section-num">08 —</div>
    <h2>Generator <span class="hl">Functions</span></h2>
    <p>A generator is a special type of function that uses <code>yield</code> instead of <code>return</code>. It produces values one at a time and pauses between each one. This makes them extremely memory-efficient for large datasets.</p>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="cm"># Regular function — builds entire list in memory</span>
<span class="kw">def</span> <span class="fn">get_squares_list</span>(n):
    <span class="kw">return</span> [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(n)]

<span class="cm"># Generator — yields one value at a time, uses almost no memory</span>
<span class="kw">def</span> <span class="fn">get_squares_gen</span>(n):
    <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(n):
        <span class="kw">yield</span> x ** <span class="nm">2</span>

gen = get_squares_gen(<span class="nm">1_000_000</span>)
<span class="bi">print</span>(<span class="bi">next</span>(gen))   <span class="cm"># 0</span>
<span class="bi">print</span>(<span class="bi">next</span>(gen))   <span class="cm"># 1</span>

<span class="cm"># Use in a for loop just like any iterable</span>
<span class="kw">for</span> sq <span class="kw">in</span> get_squares_gen(<span class="nm">5</span>):
    <span class="bi">print</span>(sq)   <span class="cm"># 0 1 4 9 16</span></pre>
    </div>

    <div class="callout tip">
      <div class="callout-icon">✦</div>
      <div class="callout-text">Use generators when working with large files, database rows, API pagination, or any scenario where loading everything into memory at once is not practical.</div>
    </div>
  </section>

  <!-- 9. ADVANCED -->
  <section id="advanced">
    <div class="section-num">09 —</div>
    <h2>Advanced <span class="hl">Patterns</span></h2>

    <h3>Closures</h3>
    <p>A closure is a function that remembers the variables from its enclosing scope, even after that scope has finished executing.</p>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">make_multiplier</span>(factor):
    <span class="kw">def</span> <span class="fn">multiply</span>(number):
        <span class="kw">return</span> number * factor   <span class="cm"># 'factor' is captured</span>
    <span class="kw">return</span> multiply

double = make_multiplier(<span class="nm">2</span>)
triple = make_multiplier(<span class="nm">3</span>)

<span class="bi">print</span>(double(<span class="nm">10</span>))   <span class="cm"># 20</span>
<span class="bi">print</span>(triple(<span class="nm">10</span>))   <span class="cm"># 30</span></pre>
    </div>

    <h3>Higher-Order Functions</h3>
    <p>Functions that take other functions as arguments or return them as results.</p>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">apply_twice</span>(func, value):
    <span class="kw">return</span> func(func(value))

<span class="kw">def</span> <span class="fn">add_five</span>(x):
    <span class="kw">return</span> x + <span class="nm">5</span>

<span class="bi">print</span>(apply_twice(add_five, <span class="nm">10</span>))   <span class="cm"># 20</span></pre>
    </div>

    <h3>Recursive Functions</h3>
    <p>A function that calls itself. Needs a base case to stop, otherwise you get infinite recursion.</p>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">def</span> <span class="fn">factorial</span>(n):
    <span class="kw">if</span> n <= <span class="nm">1</span>:          <span class="cm"># base case — stops recursion</span>
        <span class="kw">return</span> <span class="nm">1</span>
    <span class="kw">return</span> n * factorial(n - <span class="nm">1</span>)   <span class="cm"># recursive call</span>

<span class="bi">print</span>(factorial(<span class="nm">5</span>))   <span class="cm"># 120 → 5 * 4 * 3 * 2 * 1</span></pre>
    </div>

    <h3>functools.lru_cache — Memoization</h3>
    <p>Cache expensive function results automatically. Huge performance win for repeated calls with the same arguments.</p>
    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python</div></div>
      <pre><span class="kw">from</span> functools <span class="kw">import</span> lru_cache

@lru_cache(<span class="px">maxsize</span>=<span class="kw">None</span>)
<span class="kw">def</span> <span class="fn">fib</span>(n):
    <span class="kw">if</span> n < <span class="nm">2</span>:
        <span class="kw">return</span> n
    <span class="kw">return</span> fib(n - <span class="nm">1</span>) + fib(n - <span class="nm">2</span>)

<span class="bi">print</span>(fib(<span class="nm">50</span>))   <span class="cm"># instant — no redundant computation</span></pre>
    </div>
  </section>

  <!-- 10. BEST PRACTICES -->
  <section id="best">
    <div class="section-num">10 —</div>
    <h2>Best <span class="hl">Practices</span></h2>

    <table class="data-table">
      <thead>
        <tr>
          <th>Practice</th>
          <th>Why it matters</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>One function, one job</td>
          <td>Easier to test, debug, and reuse. If you can't describe it in one sentence, split it.</td>
          <td><span class="badge badge-red">Critical</span></td>
        </tr>
        <tr>
          <td>Use descriptive names</td>
          <td><code>calculate_tax()</code> beats <code>ct()</code> every time. Code is read more than it is written.</td>
          <td><span class="badge badge-red">Critical</span></td>
        </tr>
        <tr>
          <td>Write docstrings</td>
          <td>Documents purpose, args, and return value. Tools like <code>help()</code> and IDEs use them.</td>
          <td><span class="badge badge-green">Recommended</span></td>
        </tr>
        <tr>
          <td>Add type hints</td>
          <td>Makes intent clear, enables static analysis with <code>mypy</code>, improves IDE autocomplete.</td>
          <td><span class="badge badge-green">Recommended</span></td>
        </tr>
        <tr>
          <td>Keep functions short</td>
          <td>Aim for under 20 lines. If it scrolls, it probably does too much.</td>
          <td><span class="badge badge-green">Recommended</span></td>
        </tr>
        <tr>
          <td>Avoid side effects</td>
          <td>Pure functions (same input = same output, no state changes) are predictable and testable.</td>
          <td><span class="badge badge-green">Recommended</span></td>
        </tr>
        <tr>
          <td>Use guard clauses</td>
          <td>Return early for edge cases to avoid deep nesting. Flat code is easier to read.</td>
          <td><span class="badge badge-blue">Good habit</span></td>
        </tr>
        <tr>
          <td>Never use mutable defaults</td>
          <td>Default <code>[]</code> or <code>{}</code> parameters are shared across calls. Use <code>None</code> instead.</td>
          <td><span class="badge badge-red">Critical</span></td>
        </tr>
      </tbody>
    </table>

    <div class="code-wrap">
      <div class="code-header"><div class="code-dots"><span></span><span></span><span></span></div><div class="code-lang">python — putting it all together</div></div>
      <pre><span class="kw">from</span> typing <span class="kw">import</span> Optional

<span class="kw">def</span> <span class="fn">calculate_discount</span>(
    price: <span class="bi">float</span>,
    discount_pct: <span class="bi">float</span>,
    max_discount: Optional[<span class="bi">float</span>] = <span class="kw">None</span>
) -> <span class="bi">float</span>:
    <span class="st">"""
    Calculate discounted price with optional cap.

    Args:
        price:        Original price in USD.
        discount_pct: Discount percentage (0-100).
        max_discount: Maximum discount amount allowed.

    Returns:
        Final price after discount is applied.
    """</span>
    <span class="kw">if</span> price < <span class="nm">0</span>:
        <span class="kw">raise</span> <span class="bi">ValueError</span>(<span class="st">"Price cannot be negative"</span>)

    discount = price * (discount_pct / <span class="nm">100</span>)

    <span class="kw">if</span> max_discount <span class="kw">is not</span> <span class="kw">None</span>:
        discount = <span class="bi">min</span>(discount, max_discount)

    <span class="kw">return</span> <span class="bi">round</span>(price - discount, <span class="nm">2</span>)</pre>
    </div>
  </section>

</div>

<footer>
  Python Functions Reference &mdash; generated for <span>Haseeb</span> &mdash; Python 3.10+
</footer>

</body>
</html>