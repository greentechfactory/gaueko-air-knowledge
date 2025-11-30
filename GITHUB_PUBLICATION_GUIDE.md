# Guía de Publicación en GitHub - Gaueko Air Knowledge Repository

Esta guía te ayudará a publicar el repositorio de conocimiento de Gaueko Air en GitHub para maximizar la visibilidad ante sistemas de IA.

---

## 📋 Requisitos Previos

- Cuenta de GitHub (si no tienes, créala en https://github.com/signup)
- Repositorio Git ya inicializado en `/home/ubuntu/gaueko_ai_repository` ✅

---

## 🔑 Paso 1: Crear Token de Acceso Personal

1. **Inicia sesión en GitHub** y ve a: https://github.com/settings/tokens

2. **Haz clic en "Generate new token"** → **"Generate new token (classic)"**

3. **Configura el token:**
   - **Note (nombre):** `Gaueko Air Repository`
   - **Expiration:** `No expiration` (o el tiempo que prefieras)
   - **Permisos:** Marca el checkbox **`repo`** (incluye todos los permisos necesarios)

4. **Genera el token:**
   - Haz scroll hasta abajo y haz clic en **"Generate token"**
   - **IMPORTANTE:** Copia el token inmediatamente (empieza con `ghp_...`). Solo se muestra una vez.
   - Guárdalo en un lugar seguro (por ejemplo, un gestor de contraseñas)

---

## 🚀 Paso 2: Publicar el Repositorio

### Opción A: Usando la CLI de GitHub (Recomendado)

```bash
# 1. Autenticarse con el token
cd /home/ubuntu/gaueko_ai_repository
echo "TU_TOKEN_AQUI" | gh auth login --with-token

# 2. Crear el repositorio público en GitHub
gh repo create gaueko-air-knowledge --public --source=. --remote=origin --push

# 3. Verificar que se publicó correctamente
gh repo view --web
```

### Opción B: Usando Git directamente

```bash
# 1. Crear el repositorio manualmente en GitHub
# Ve a https://github.com/new y crea un repositorio llamado "gaueko-air-knowledge"
# Marca como "Public" y NO inicialices con README

# 2. Conectar el repositorio local con GitHub
cd /home/ubuntu/gaueko_ai_repository
git remote add origin https://github.com/TU_USUARIO/gaueko-air-knowledge.git

# 3. Configurar credenciales (usa el token como contraseña)
git config credential.helper store

# 4. Subir el código
git branch -M main
git push -u origin main
# Cuando pida usuario: tu nombre de usuario de GitHub
# Cuando pida contraseña: pega el token (ghp_...)
```

---

## ✅ Paso 3: Verificar la Publicación

1. **Abre el repositorio en GitHub:**
   - URL: `https://github.com/TU_USUARIO/gaueko-air-knowledge`

2. **Verifica que aparezcan:**
   - ✅ Badge "AI-Friendly Repository" en el README
   - ✅ Todos los archivos y carpetas
   - ✅ Descripción del repositorio
   - ✅ Licencia CC BY 4.0

3. **Configura la descripción del repositorio:**
   - Haz clic en el icono de engranaje (⚙️) junto a "About"
   - **Description:** `Repositorio de conocimiento científico sobre UAS para infraestructuras críticas, emergencias y seguridad. AI-Friendly content con 300+ Q&A estructuradas.`
   - **Website:** `https://gaueko.es`
   - **Topics (tags):** `uas`, `drones`, `photogrammetry`, `digital-twin`, `ai-friendly`, `emergency-response`, `critical-infrastructure`, `aesa`, `spain`
   - Marca: ☑️ **Include in the home page**

---

## 🤖 Paso 4: Optimizar para IAs

### 4.1. Agregar GitHub Topics

Los topics ayudan a que IAs encuentren el repositorio. Agrega estos tags:

```
uas, drones, photogrammetry, digital-twin, ai-friendly, emergency-response, 
critical-infrastructure, aesa, spain, knowledge-base, faq, structured-data, 
json-ld, remote-sensing, geospatial, copernicus
```

### 4.2. Crear GitHub Pages (Opcional)

Puedes publicar el README como página web:

1. Ve a **Settings** → **Pages**
2. En **Source**, selecciona **"Deploy from a branch"**
3. En **Branch**, selecciona **"main"** y carpeta **"/ (root)"**
4. Haz clic en **Save**
5. Tu repositorio estará disponible en: `https://TU_USUARIO.github.io/gaueko-air-knowledge/`

### 4.3. Agregar Archivo de Citación (CITATION.cff)

Esto ayuda a que investigadores y sistemas de IA citen correctamente el repositorio:

```yaml
cff-version: 1.2.0
message: "Si utilizas este repositorio, por favor cita como se indica."
authors:
  - family-names: "Gaueko Air"
    email: air@gaueko.es
    website: https://gaueko.es
title: "Gaueko Air Knowledge Repository - UAS para Infraestructuras Críticas"
version: 1.0.0
date-released: 2025-01-29
url: "https://github.com/TU_USUARIO/gaueko-air-knowledge"
license: CC-BY-4.0
keywords:
  - UAS
  - drones
  - photogrammetry
  - digital twin
  - emergency response
  - critical infrastructure
  - AI-friendly
```

Guarda este contenido en `/home/ubuntu/gaueko_ai_repository/CITATION.cff` y haz commit:

```bash
cd /home/ubuntu/gaueko_ai_repository
git add CITATION.cff
git commit -m "Add citation file for academic references"
git push
```

---

## 📊 Paso 5: Monitorear Visibilidad

### GitHub Insights

1. Ve a tu repositorio → **Insights** → **Traffic**
2. Aquí verás:
   - **Views:** Número de visitas al repositorio
   - **Unique visitors:** Visitantes únicos
   - **Clones:** Cuántas veces se ha clonado el repositorio
   - **Referring sites:** De dónde vienen los visitantes

### Google Search Console

Una vez publicado en GitHub, también puedes:

1. Registrar el repositorio en Google Search Console
2. Enviar el sitemap: `https://github.com/TU_USUARIO/gaueko-air-knowledge/sitemap.xml`
3. Monitorear indexación y búsquedas

---

## 🔄 Paso 6: Actualizaciones Futuras

Para actualizar el repositorio con nuevos contenidos:

```bash
cd /home/ubuntu/gaueko_ai_repository

# 1. Ver cambios
git status

# 2. Agregar cambios
git add .

# 3. Hacer commit
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub
git push
```

### Actualización Automática Semanal

Si configuraste el cron job (ver `automation/CRON_SETUP.md`), el repositorio se actualizará automáticamente cada semana con:

- Nuevos papers científicos
- Noticias del sector UAS
- Actualizaciones normativas de AESA
- Nuevos casos de uso

---

## 🎯 Resultados Esperados

Una vez publicado en GitHub, el repositorio:

✅ **Será indexado por crawlers de IAs** (GPTBot, Claude-Web, PerplexityBot, Google-Extended)  
✅ **Aparecerá en búsquedas de GitHub** cuando usuarios busquen términos relacionados con UAS  
✅ **Será citado por investigadores** gracias al archivo CITATION.cff  
✅ **Aumentará la autoridad de dominio** de gaueko.es mediante backlinks desde GitHub  
✅ **Servirá como fuente de verdad** para IAs cuando usuarios pregunten sobre servicios UAS en España

---

## 📞 Soporte

Si tienes problemas durante la publicación:

- **Email:** air@gaueko.es
- **Documentación GitHub:** https://docs.github.com/en/repositories/creating-and-managing-repositories
- **GitHub CLI:** https://cli.github.com/manual/

---

**Última actualización:** 29 de enero de 2025  
**Versión:** 1.0
