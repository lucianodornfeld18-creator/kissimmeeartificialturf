# Auditoria de 60 pontos — kissimmeeartificialturf.com

Data: 2026-09-23. Site publicado em https://kissimmeeartificialturf.pages.dev (578 páginas, 60 cidades). Domínio próprio pendente do DNS do dono. Legenda: **PASS** verificado com evidência · **PARCIAL** feito em parte · **FAIL** não feito · **BLOCKED** depende de acesso que não tenho · **OWNER INPUT** depende de decisão ou dado do dono.

## Pesquisa e estratégia (1–10)

| # | Ponto | Status | Evidência |
|---|---|---|---|
| 1 | Keyword Planner exportado com configuração | **BLOCKED** | Sem conta Google Ads autenticada nesta máquina. O universo de keywords veio de pesquisa web, PAA e concorrentes (`docs/WRITING-GUIDE.md`, prompt seção 4.1). Se o dono exportar o CSV, entra em `research/`. |
| 2 | Mapa keyword → URL única | **PASS** | `research/titles-metas.csv` (578 linhas, 0 títulos ou H1 duplicados); registry de slugs em `site/_posts.py`. |
| 3 | Concorrentes reauditados | **PASS** | Tabela na seção 4.3 do prompt (2026-09-21): nenhum concorrente local tem FAQ, blog, tabela de preço, lei HB 683 ou permits. |
| 4 | SERP / AI Overview por cluster | **FAIL** | Não foi feito de forma sistemática por cluster e cidade. Fazer em janela anônima com localização Kissimmee depois da indexação. |
| 5 | 60 prompts de IA testados com fontes | **FAIL** | Não executado. Só faz sentido depois de o domínio próprio estar indexado; antes disso as IAs não citam o site. |
| 6 | 120+ perguntas classificadas por evidência | **PARCIAL** | 1.700 entidades `Question` no schema (87 no FAQ hub, 4–8 por página comercial, 3–5 por post). A classificação por evidência (PAA / Reddit / AI-CITED) ficou nos briefs dos redatores, não num CSV. |
| 7 | 70 perguntas obrigatórias, cada uma numa URL dona | **PASS** | As 70 da seção 5 do prompt foram distribuídas por módulo (`c_faq`, `c_posts_a–d`, `c_services_*`, `c_pricing`, `c_laws`, `c_permits`, `c_compare`); o FAQ hub só resume e linka quando outra página é dona. |
| 8 | Fatos legais revalidados com data | **PASS** | Regra DEP 62-308.100 ADOTADA (efetiva 2026-05-19), texto final em `research/dep-62-308.100-final.txt`; F.S. 125.572, 720.3045, 720.3075 conferidos em 2026-09-21/22. O prompt dizia "proposta"; o site diz o status real. |
| 9 | Preços revalidados ou do dono | **OWNER INPUT** | Faixas de mercado com fonte e data (set/2026) em todas as tabelas. Preços reais do dono substituem `PRICES` em `site/_data.py`. |
| 10 | Histórico do domínio | **PASS** | RDAP (Verisign): registrado em 2026-09-07 na Cloudflare, expira 2027-09-07. Wayback: nenhuma captura. Domínio novo, sem histórico tóxico. |

## Entidade e verdade (11–18)

| # | Ponto | Status | Evidência |
|---|---|---|---|
| 11 | Nome público exato "Kissimmee Artificial Turf" | **PASS** | Header, footer, `WebSite.name`, `og:site_name`, assunto do e-mail, marca no opera-portal. |
| 12 | Zero fato inventado | **PASS** | Regra "never invent" no guia; QA barra frases de histórico (`TRACK`); cada redator listou o que não conseguiu verificar e deixou fora. Endereço, licença, avaliações, anos de mercado e fotos: nenhum. |
| 13 | Licença/seguro só com prova | **PASS** | O site não diz "licensed" nem "insured". O post `do-turf-installers-need-a-license-in-florida` explica o cenário sem afirmar o nosso. |
| 14 | Schema sem rua/geo/rating/horário inventados | **PASS** | `HomeAndConstructionBusiness` só com `addressLocality/Region/Country`, telefone, `founder`, `foundingDate: 2024` (da logo). Sem `AggregateRating`, `Review`, `GeoCoordinates`, `openingHours`. |
| 15 | Dono/autor real | **PASS** | Luis Austin em `/about/`, na assinatura de toda página comercial e em `BlogPosting.author`. |
| 16 | Zero termo de captação ou nota interna no `dist/` | **PASS** | Lista `INTERNAL` no QA (lead generation, sister, hub_id, keyword, tier, pipeline…): 0 ocorrências. |
| 17 | Fotos exclusivas ou ilustração própria | **OWNER INPUT** | Sem fotos de obra. Hero = logo em vetor; diagrama SVG de camadas. Fotos da rede de concreto NÃO foram usadas. `/gallery/` não existe. |
| 18 | OWNER-INPUTS completo e fora do build | **PASS** | `docs/OWNER-INPUTS.md`; grep de "pending" e "OWNER-INPUTS" no dist = 0. |

## Arquitetura e conteúdo (19–36)

| # | Ponto | Status | Evidência |
|---|---|---|---|
| 19 | 12 serviços completos | **PASS** | 12 páginas, 2.192–2.658 palavras, tabela + passos + preço + lei + FAQ em cada uma. |
| 20 | City hubs com dados locais | **PASS** | 60 hubs, 1.238–2.318 palavras, cada um com órgão de alvará, concessionária de água, distrito, solo USDA, lagos e comunidades citados. |
| 21 | Cidade × serviço com gate de unicidade | **PASS** | 420 páginas (T1 15×12, T2 35×6, T3 10×3), 1.219–1.712 palavras; cada uma com 3 seções locais + cenário + FAQ próprios sobre o banco de blocos. |
| 22 | 8-grams < 15% interno | **PASS** | `qa_all.py --sim`: 0 pares > 15%, medindo texto próprio E texto total (banco incluído). |
| 23 | 8-grams vs kissimmeeconcrete.com e GCM | **PASS** | `/pavers/artificial-turf/` (kissimmeeconcrete) e `/artificial-turf/` (GCM) vs home, `/turf-and-pavers/`, `/artificial-grass-installation/`, `/pet-turf/`: 0 8-grams compartilhados. |
| 24 | Hub de preços + 11 tabelas | **PASS** | 5 tabelas no hub de custo + 163 no resto do site (168 no total): por serviço, por tamanho, composição do preço, 10 anos, infill, pile/face weight, temperatura com fontes, calendário de manutenção, garantia, regra por jurisdição, rega. |
| 25 | 40+ posts | **PASS** | 41 posts, 1.332–1.597 palavras. |
| 26 | FAQ hub 60+ | **PASS** | 87 perguntas em 5 páginas. |
| 27 | 70 perguntas publicadas, uma URL cada | **PASS** | Ver ponto 7; `FAQPage` só na URL dona (o hub reformula a pergunta quando resume). |
| 28 | Cápsulas de 40–70 palavras | **PASS** | Checado por `qa/check_module.py` em todo módulo. |
| 29 | Hub legal com status real do DEP | **PASS** | `/laws/florida-hb-683/`: linha do tempo, tabela com as exigências da regra, o que a lei NÃO faz. |
| 30 | Permits por jurisdição com fonte oficial | **PASS** | 8 páginas + `research/permits-research.md`. Só a City of Orlando tem código de turf (fonte secundária, avisado na página); os outros 7 não publicam nada e cada página diz isso. |
| 31 | Comparações | **PASS** | 7 páginas. |
| 32 | Ferramentas sem JS pesado | **PASS** | Calculadora de custo/materiais, turf vs sod 10 anos, checklist de HOA; JS de 4 KB, sem framework. |
| 33 | "best/near me" dentro dos limites | **PASS** | Sempre como pergunta do cliente; home 2, serviço 1, hub 1, cidade×serviço ≤ 4 por cidade, 2 posts com "best" no título. QA avisa acima de 3 por página. |
| 34 | Densidade de keyword | **PASS** | QA: 0 páginas acima de 3,5% de "artificial turf/grass". |
| 35 | Checagem de estilo anti-IA | **PASS** | Lista de 50 frases proibidas, exclamações, travessões, "ensure": 0 FAIL. |
| 36 | Contagem de palavras por tipo | **PASS** | Pisos por tipo em `qa_all.py`; as únicas abaixo são index/tool/legal, por desenho. |

## On-page e técnico (37–50)

| # | Ponto | Status | Evidência |
|---|---|---|---|
| 37 | Title/H1/meta únicos | **PASS** | 578/578 únicos; titles ≤ 65 caracteres; metas 110–165. |
| 38 | Canonical e redirects | **PASS** | Canonical autorreferente em toda página; `_redirects` (index.html, /cost/, /pricing/). |
| 39 | Sitemap, robots, llms, feed | **PASS** | `sitemap.xml` (índice por seção), `robots.txt`, `llms.txt`, `llms-full.txt`, `feed.xml`, chave IndexNow publicada. |
| 40 | Zero link quebrado, órfã ou cadeia | **PASS** | QA: 0 links quebrados; `soften_links` transforma link para página inexistente em texto; toda página tem inlink (as legais só pelo footer). |
| 41 | Inlinks ≥ 3 e ≤ 3 cliques | **PASS** | Só `/terms/` e `/accessibility/` (footer) ficam abaixo de 3 links contextuais. Profundidade: home → hub → cidade → cidade×serviço. |
| 42 | Breadcrumbs + `BreadcrumbList` | **PASS** | Em toda página interna. |
| 43 | JSON-LD válido | **PASS** | Parseado nas 578 páginas pelo QA. Não passou pelo Rich Results Test (fazer depois do domínio). |
| 44 | Lighthouse mobile 100/100/100/100 | **PARCIAL** | Em 6 tipos de página: Performance 96–99, Acessibilidade 100, Boas práticas 100, SEO 66–69 **só por causa do `noindex` proposital no pages.dev**. No domínio próprio, o único item de SEO que falha (`is-crawlable`) some. |
| 45 | Lighthouse desktop | **PASS** | 98 / 100 / 100 / (69 pelo mesmo motivo); LCP 0,4–0,5 s. |
| 46 | Core Web Vitals | **PASS** | LCP 1,1–2,0 s mobile, CLS 0, TBT 0–20 ms. |
| 47 | WCAG 2.2 AA | **PASS** | Lighthouse acessibilidade 100 em todas as amostras; landmarks, labels, foco visível, alvos ≥ 44 px, tabelas com caption e th. |
| 48 | Headers/CSP | **PASS** | `_headers` com CSP por hash, HSTS, nosniff, Referrer-Policy, Permissions-Policy. |
| 49 | HTML ≤ 150 KB | **PASS** | Máximo 66 KB, mediana 34 KB. |
| 50 | Crawlers de busca e IA liberados | **PARCIAL** | `robots.txt` libera Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, ClaudeBot, GPTBot etc. O WAF do Cloudflare ("Block AI bots") precisa ser conferido pelo dono no painel. |

## Conversão e operação (51–60)

| # | Ponto | Status | Evidência |
|---|---|---|---|
| 51 | Número Twilio apontado para `kissimmeeturf-voice` | **BLOCKED** | Sem Account SID/Auth Token. Código e `twilio/deploy_kissimmeeturf_voice.py` prontos. |
| 52 | 4 handlers testados com assinatura | **BLOCKED** | Idem. |
| 53 | Ligação real com gravação e transcrição | **BLOCKED** | Idem. |
| 54 | SMS de entrada no painel | **BLOCKED** | Idem (e A2P 10DLC pendente na conta). |
| 55 | `hello@` recebendo | **PASS** | Email Routing `ready`, MX `route1/2/3.mx.cloudflare.net` e SPF no DNS público; hello@/info@/quotes@ + catch-all → opusdigitalmarketingflorida@gmail.com. O dono deve confirmar o recebimento de um e-mail de teste. |
| 56 | Formulário + honeypot + consentimento | **PASS** | Envio em Chrome real aceito pelo Web3Forms (2026-09-21, "TESTE automatico do site"); honeypot `botcheck`, checkbox de consentimento, entrega em `/thank-you/` próprio. Chave provisória do Kissimmee Concrete (OWNER INPUT). |
| 57 | Espelho no opera-portal testado e lead de teste apagado | **PASS** | Marca `kissimmee-turf` (id 8); lead honeypot chegou como `spam` e foi apagado por id. |
| 58 | Pages git-linked, domínio e www com SSL | **BLOCKED** | Projeto criado por API e ligado ao GitHub; domínio e www anexados, status `pending: CNAME record not set`. O dono cria 2 CNAME. |
| 59 | Search Console + Bing + IndexNow | **BLOCKED** | Dependem do domínio ativo (TXT no DNS). Chave IndexNow já publicada. |
| 60 | Reauditoria final limpa | **PASS** | `qa_all.py --sim` em 578 páginas: FAIL 0; 0 pares > 15%. |

```text
Domain: kissimmeeartificialturf.com
Build date:                2026-09-23
Indexable URLs:            576 (578 páginas menos thank-you e 404): 12 services / 5 counties / 60 city hubs / 420 city×service / 41 posts / 5 FAQ / 7 compare / 9 permits / 3 laws / 1 price + tools, indexes, legal
Questions answered:        87 no FAQ hub + 1.613 em FAQs contextuais = 1.700 entidades Question (mínimo pedido: 70)
Lighthouse mobile median:  P97 A100 BP100 SEO66-69 (SEO sobe a 100 no domínio próprio; o único item que falha é o noindex do pages.dev)
60-point result:           43 PASS · 4 PARCIAL (6, 44, 50 + 55 a confirmar) · 2 FAIL (4, 5) · 8 BLOCKED (1, 51-54, 58, 59) · 3 OWNER INPUT (9, 17, chave do 56)
Blocked items:             DNS (2 CNAME), credenciais Twilio, Keyword Planner
Owner inputs still required: ver docs/OWNER-INPUTS.md
Cannibalization decisions pending: nenhuma; kissimmeeconcrete.com/pavers/artificial-turf/ e GCM /artificial-turf/ mantidos, 0 8-grams em comum
Deployment status:         DEPLOYED em pages.dev (noindex); READY para o domínio assim que o DNS for criado
```
