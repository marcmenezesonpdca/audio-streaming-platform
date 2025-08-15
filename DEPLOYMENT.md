# Guia de Implantação - Plataforma de Streaming de Áudio

Este guia fornece instruções passo a passo para implantar a plataforma em serviços gratuitos de hospedagem.

## Opções de Hospedagem Gratuita

### 1. Render.com (Recomendado)
- ✅ Plano gratuito generoso
- ✅ Deploy automático via GitHub
- ✅ SSL gratuito
- ✅ Suporte nativo ao Python/Flask

### 2. Railway.app
- ✅ Interface intuitiva
- ✅ Deploy via GitHub
- ✅ Boa performance
- ✅ Plano gratuito adequado para MVPs

### 3. Heroku (Alternativa)
- ✅ Tradicional e confiável
- ⚠️ Plano gratuito limitado
- ✅ Boa documentação

---

## Implantação no Render.com

### Passo 1: Preparação do Código

1. **Crie um repositório no GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Audio Streaming Platform"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/audio-streaming-platform.git
   git push -u origin main
   ```

2. **Certifique-se de que o `requirements.txt` está atualizado:**
   ```bash
   source venv/bin/activate
   pip freeze > requirements.txt
   ```

### Passo 2: Configuração no Render

1. **Acesse [render.com](https://render.com) e crie uma conta**

2. **Clique em "New +" → "Web Service"**

3. **Conecte seu repositório GitHub**

4. **Configure o serviço:**
   - **Name:** `audio-streaming-platform`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python src/main.py`
   - **Plan:** `Free`

5. **Variáveis de ambiente (opcional):**
   - `FLASK_ENV=production`
   - `SECRET_KEY=sua_chave_secreta_aqui`

6. **Clique em "Create Web Service"**

### Passo 3: Configuração de Domínio

Após o deploy, você receberá uma URL como:
```
https://audio-streaming-platform.onrender.com
```

---

## Implantação no Railway.app

### Passo 1: Preparação

1. **Crie um arquivo `railway.json` na raiz do projeto:**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python src/main.py",
       "healthcheckPath": "/api/events"
     }
   }
   ```

2. **Certifique-se de que o código está no GitHub**

### Passo 2: Deploy no Railway

1. **Acesse [railway.app](https://railway.app) e faça login**

2. **Clique em "New Project" → "Deploy from GitHub repo"**

3. **Selecione seu repositório**

4. **Configure as variáveis de ambiente (se necessário):**
   - `PORT=5000`
   - `FLASK_ENV=production`

5. **O deploy será automático**

---

## Configuração de Banco de Dados para Produção

### Opção 1: SQLite (Simples, adequado para MVPs)
- ✅ Já configurado no projeto
- ✅ Sem configuração adicional necessária
- ⚠️ Dados podem ser perdidos em redeploys

### Opção 2: PostgreSQL Gratuito

#### No Render.com:
1. **Crie um PostgreSQL database:**
   - Vá para Dashboard → "New +" → "PostgreSQL"
   - Nome: `audio-streaming-db`
   - Plan: Free

2. **Atualize as variáveis de ambiente:**
   ```
   DATABASE_URL=postgresql://user:password@host:port/database
   ```

3. **Modifique `src/main.py`:**
   ```python
   import os
   
   # Configuração do banco
   if os.environ.get('DATABASE_URL'):
       app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
   else:
       app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
   ```

---

## Configuração de Streaming de Áudio

### Opções Gratuitas para Streaming HLS:

#### 1. YouTube Live (Recomendado para testes)
- ✅ Gratuito e confiável
- ✅ Gera URLs HLS automaticamente
- ✅ Boa qualidade de áudio

**Como usar:**
1. Configure um stream no YouTube Live
2. Obtenha a URL do manifest HLS
3. Configure no painel administrativo

#### 2. Twitch
- ✅ Gratuito
- ✅ Baixa latência
- ✅ URLs HLS disponíveis

#### 3. Servidor próprio com FFmpeg
Para eventos menores, você pode usar um servidor próprio:

```bash
# Exemplo de comando FFmpeg para gerar HLS
ffmpeg -f alsa -i hw:0 -c:a aac -b:a 128k -f hls -hls_time 10 -hls_list_size 6 -hls_flags delete_segments output.m3u8
```

---

## Checklist Pré-Deploy

### ✅ Código
- [ ] Código commitado no GitHub
- [ ] `requirements.txt` atualizado
- [ ] Frontend buildado e copiado para `src/static/`
- [ ] Variáveis de ambiente configuradas

### ✅ Configurações
- [ ] CORS habilitado
- [ ] Servidor configurado para `0.0.0.0:5000`
- [ ] Rotas de fallback para SPA funcionando
- [ ] SSL/HTTPS configurado (automático no Render/Railway)

### ✅ Testes
- [ ] Painel administrativo funcionando
- [ ] Criação de eventos testada
- [ ] QR Codes sendo gerados
- [ ] Registro de participantes funcionando
- [ ] Player de áudio carregando

---

## Monitoramento e Logs

### No Render:
- Acesse "Logs" no dashboard do serviço
- Configure alertas de saúde da aplicação

### No Railway:
- Visualize logs em tempo real no dashboard
- Configure métricas de performance

---

## Domínio Personalizado (Opcional)

### Render.com:
1. Vá para Settings → Custom Domains
2. Adicione seu domínio
3. Configure DNS conforme instruções

### Railway.app:
1. Vá para Settings → Domains
2. Adicione domínio personalizado
3. Configure registros DNS

---

## Backup e Segurança

### Backup do Banco de Dados:
```bash
# Para SQLite
cp src/database/app.db backup_$(date +%Y%m%d).db

# Para PostgreSQL
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d).sql
```

### Segurança:
- Use HTTPS (automático nos serviços)
- Configure variáveis de ambiente para dados sensíveis
- Implemente rate limiting se necessário
- Monitore logs de acesso

---

## Solução de Problemas Comuns

### Erro 500 - Internal Server Error:
1. Verifique os logs da aplicação
2. Confirme se todas as dependências estão instaladas
3. Verifique variáveis de ambiente

### Frontend não carrega:
1. Confirme se os arquivos estão em `src/static/`
2. Verifique se as rotas de fallback estão funcionando
3. Teste localmente primeiro

### Player de áudio não funciona:
1. Verifique se a URL HLS está acessível
2. Teste a URL em um player HLS online
3. Confirme configurações CORS do servidor de streaming

### Banco de dados não inicializa:
1. Verifique permissões de escrita
2. Confirme string de conexão
3. Execute `db.create_all()` manualmente se necessário

---

## Próximos Passos Após Deploy

1. **Teste completo da aplicação**
2. **Configure monitoramento**
3. **Documente URLs de produção**
4. **Treine usuários administradores**
5. **Prepare plano de backup**
6. **Configure domínio personalizado (se desejado)**

---

## Suporte e Manutenção

### Atualizações:
- Commits no GitHub disparam redeploy automático
- Teste mudanças localmente antes do push
- Use branches para features grandes

### Escalabilidade:
- Monitore uso de recursos
- Considere upgrade para planos pagos se necessário
- Implemente cache se a aplicação crescer

### Logs e Debugging:
- Monitore logs regularmente
- Configure alertas para erros
- Mantenha backups atualizados

