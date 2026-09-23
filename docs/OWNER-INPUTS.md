# Pendências do proprietário — kissimmeeartificialturf.com

Interno. Nunca renderizado no site. Atualizado em 2026-09-23 (site com 570 paginas no ar em pages.dev; auditoria em AUDIT-60-POINT.md).

## 1. Bloqueia o domínio próprio (1 minuto, só você consegue)

O token do wrangler nesta máquina não tem permissão de DNS (erro 10000). O projeto Pages, o deploy e o anexo do domínio já estão feitos; falta só o DNS:

Cloudflare → `kissimmeeartificialturf.com` → **DNS → Records → Add record**, duas vezes:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | `@` | `kissimmeeartificialturf.pages.dev` | Proxied (laranja) |
| CNAME | `www` | `kissimmeeartificialturf.pages.dev` | Proxied (laranja) |

Alternativa: Workers & Pages → `kissimmeeartificialturf` → Custom domains → clicar no domínio pendente → "Activate domain" (o painel cria o registro sozinho).
Depois disso o certificado sai em alguns minutos. Até lá o site responde em https://kissimmeeartificialturf.pages.dev (com `noindex`, de propósito).

Se quiser que eu faça isso nas próximas vezes: crie um API token com **Zone → DNS → Edit** para esta zona e rode `set CF_API_TOKEN=...` antes de me chamar. Não guarde o token em arquivo.

## 2. Bloqueia o telefone (Twilio)

- **Account SID + Auth Token** da conta Twilio (não estão em disco em nenhum projeto). Com eles: `python twilio/deploy_kissimmeeturf_voice.py` cria o serviço `kissimmeeturf-voice`, publica os 4 handlers e aponta o (689) 202-3710. Código pronto e conferido em `twilio/`.
- **Celular que recebe as chamadas** (`FORWARD_TO`). Padrão dos hubs de Orlando: +1 689 242-7487. Confirmar se o turf toca no mesmo aparelho.
- A saudação diz "This call may be recorded". A Flórida exige consentimento de todas as partes para gravar (F.S. 934.03) e o fluxo grava a chamada. **Os outros sites (Ocoee, Windermere, Kissimmee Concrete etc.) gravam sem avisar** — vale corrigir a saudação deles também.
- Enquanto o serviço não estiver publicado, quem ligar para o número cai no que estiver configurado hoje na Twilio (provavelmente a mensagem demo). O número já aparece no site.

## 3. Formulário

- Entrega por Web3Forms usando, de forma provisória, a chave do Kissimmee Concrete (mesma caixa de entrada). O assunto vem como `[Kissimmee Artificial Turf] …`, então dá para filtrar. **Criar uma chave própria** em web3forms.com com o e-mail da opus e trocar `WEB3FORMS_KEY` em `site/_data.py`.
- Um e-mail de teste foi enviado em 2026-09-21 com o nome "TESTE automatico do site (pode apagar)". Conferir se chegou.
- Cópia de cada lead vai para o opera-portal, marca `kissimmee-turf` (id 8, região Orlando), criada em 2026-09-21. Testado com lead-robô, que foi apagado por id.

## 4. Conteúdo que só você pode fornecer

- **Fotos reais de obras de turf.** Colocar em `images/incoming/`. Sem elas o site usa a logo e diagramas próprios; não existe galeria. Não reaproveitar fotos dos sites de concreto.
- **Logo original em alta.** O selo foi redesenhado em vetor a partir da imagem enviada no chat (`brand/make_logo.py`). Se existir o arquivo original (PNG/SVG/AI), mandar para eu substituir.
- **Preços reais** (por sq ft e mínimo de obra). Hoje todas as tabelas dizem "Central Florida market range" com fonte e data.
- **Marcas/linhas de grama e infill que a empresa instala**, fornecedor, garantia de produto e de mão de obra. Sem isso o site não cita marca nem garantia, e a página `/warranty/` não existe.
- **Entidade legal e licença/seguro.** O site não diz "licensed" nem "insured". A Flórida não tem licença estadual para turf, mas anunciar como contratante sem número pode ser questionado; se houver Business Tax Receipt e apólice, eu incluo.
- **"Est. 2024"** veio da logo que você enviou e aparece no cabeçalho, na home, no About e no schema (`foundingDate`). Confirmar que está certo.
- **Google Business Profile e Yelp.** São a fonte nº 1 de citação local por IA (GBP para o Google, Yelp para o ChatGPT). Sem endereço verificável não dá para criar; decisão sua.
- **Atende em espanhol?** Se sim, entra a seção `/es/`.
- **Horário de atendimento.** Não publicado porque não foi informado.

## 5. Depois que o domínio estiver no ar

- Rodar os 60 prompts de IA (ChatGPT, Perplexity, Gemini, Copilot, AI Mode) e as SERPs por cluster (pontos 4 e 5 da auditoria); so faz sentido depois da indexacao.
- Rich Results Test em uma pagina de cada tipo (ponto 43).

- Search Console (propriedade de domínio) e Bing Webmaster: exigem um TXT no DNS, que também depende do item 1.
- Cloudflare → Scrape Shield → desligar "Email Address Obfuscation" e Speed → desligar "Rocket Loader" nesta zona (tiram pontos do Lighthouse e quebram a CSP).
- Cloudflare → Security → Bots → conferir que "Block AI bots" está desligado (o `robots.txt` libera os bots de busca e de IA; o WAF não pode contradizer).
- Cloudflare Web Analytics: ativar para o domínio (o beacon é injetado pelo Cloudflare; a CSP já permite).
