# Pendências do proprietário — kissimmeeartificialturf.com

Interno. Nunca renderizado no site. Atualizado em 2026-09-23 (domínio próprio NO AR em https://kissimmeeartificialturf.com; 579 páginas com as 9 fotos; auditoria em AUDIT-60-POINT.md).

## 1. Domínio próprio: FEITO em 2026-09-23

Você criou os dois CNAME no painel e o domínio ficou ativo com certificado em minutos. `www.kissimmeeartificialturf.com` também abre o site (o canonical de todas as páginas aponta para o domínio sem www) e `kissimmeeartificialturf.pages.dev` continua com `noindex`. O `_redirects` do Pages não faz redirecionamento por domínio (limitação documentada pela Cloudflare); se quiser o www respondendo 301, é 1 minuto no painel: Cloudflare → `kissimmeeartificialturf.com` → Rules → Redirect Rules → Create rule → modelo "Redirect from WWW to root" → Deploy. IndexNow: enviado em 2026-09-23 com as 577 URLs do sitemap (Bing, Yandex, Naver e Seznam; o Google não usa IndexNow). E-mail: a "Email Address Obfuscation" da zona está ligada, mas o build envolve os endereços em `<!--email_off-->`, então robôs e IAs leem o e-mail real (verificado no ar). Lighthouse no domínio final (mobile): home 96/100/100/100, página cidade×serviço 98/100/100/100.

Continua valendo: meu token do wrangler não altera DNS nem configurações da zona. Se um dia quiser que eu faça isso, crie um API token com **Zone → DNS → Edit** (e, se for o caso, Zone Settings → Edit) e rode `set CF_API_TOKEN=...` antes de me chamar. Não guarde o token em arquivo.

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

- **Fotos: 9 recebidas em 2026-09-23 e já no ar** (hero da home, faixa de miniaturas, `/gallery/`, 8 páginas de serviço, About e 3 posts). Originais ficam em `images/incoming/` (fora do git); as versões otimizadas em `site/static/img/photos/` (WebP em 3–4 larguras, miniaturas 4:3, JPEG 1200×630 para WhatsApp/Facebook, nomes com marca + assunto, sem metadados). Nenhuma legenda cita cidade ou bairro porque isso não foi informado. Para confirmar:
  - **Confirmado em 2026-09-23:** as 9 são obras da própria empresa; manter tudo (a foto com a pessoa ao fundo e as duas de cobertura ficam). O site agora diz "our own installations" na home e na galeria.
  - Só para saber responder a cliente: a foto sob a magnólia mostra turf dentro da copa da árvore, e as duas de beira de lago mostram turf perto da água. A regra estadual em vigor desde 19/05/2026 pede laudo de arborista para turf sob copa e 10 pés de recuo de lago sem seawall; obra anterior à regra, ou fora de lote unifamiliar, está fora do alcance dela.
  - Fotos novas: copiar para `images/incoming/`, registrar em `site/_photos.py` (nome SEO, alt, ponto focal, serviços) e rodar `python brand/make_photos.py`; depois usar `photo("id", "legenda")` nas páginas.
- **Logo original em alta.** O selo foi redesenhado em vetor a partir da imagem enviada no chat (`brand/make_logo.py`). O arquivo `Kissimmee_Artificial_Turf_Logo_Option_11.png` que estava em Downloads é um print cortado (o topo do selo fica fora da imagem), então não serve como original; se existir o arquivo do designer (PNG grande, SVG ou AI), mandar para eu substituir.
- **Preços reais** (por sq ft e mínimo de obra). Hoje todas as tabelas dizem "Central Florida market range" com fonte e data.
- **Marcas/linhas de grama e infill que a empresa instala**, fornecedor, garantia de produto e de mão de obra. Sem isso o site não cita marca nem garantia, e a página `/warranty/` não existe.
- **Entidade legal e licença/seguro.** O site não diz "licensed" nem "insured". A Flórida não tem licença estadual para turf, mas anunciar como contratante sem número pode ser questionado; se houver Business Tax Receipt e apólice, eu incluo.
- **"Est. 2024"** veio da logo que você enviou e aparece no cabeçalho, na home, no About e no schema (`foundingDate`). Confirmar que está certo.
- **Google Business Profile e Yelp.** São a fonte nº 1 de citação local por IA (GBP para o Google, Yelp para o ChatGPT). Sem endereço verificável não dá para criar; decisão sua.
- **Atende em espanhol?** Se sim, entra a seção `/es/`.
- **Horário de atendimento.** Não publicado porque não foi informado.

## 5. Depois que o domínio estiver no ar

- Rodar os 60 prompts de IA (ChatGPT, Perplexity, Gemini, Copilot, AI Mode) e as SERPs por cluster (pontos 4 e 5 da auditoria); só faz sentido umas semanas depois da indexação.
- Rich Results Test em uma pagina de cada tipo (ponto 43), incluindo `/gallery/` (ImageGallery + ImageObject).
- Search Console → Imagens: o sitemap já leva `<image:image>` para as 9 fotos; conferir se o Google indexou as imagens depois de algumas semanas.

- **Google Search Console** (só você, com a conta Google): https://search.google.com/search-console → Adicionar propriedade → tipo **Domínio** → `kissimmeeartificialturf.com` → o Google mostra um registro **TXT** → Cloudflare → DNS → Add record (Type TXT, Name `@`, Content colado) → Verificar. Depois: Sitemaps → enviar `https://kissimmeeartificialturf.com/sitemap.xml`. Se quiser que eu acompanhe, adicione lucianodornfeld18@gmail.com como usuário da propriedade.
- **Bing Webmaster Tools**: https://www.bing.com/webmasters → Importar do Google Search Console (1 clique depois do item acima).
- Cloudflare → Scrape Shield / Speed: verificado em 2026-09-23 no domínio final. Rocket Loader está desligado; a ofuscação de e-mail está ligada, mas o build já protege os endereços, então nada a fazer.
- Cloudflare → Security → Bots → conferir que "Block AI bots" está desligado (o `robots.txt` libera os bots de busca e de IA; o WAF não pode contradizer).
- Cloudflare Web Analytics: ativar para o domínio (o beacon é injetado pelo Cloudflare; a CSP já permite).
