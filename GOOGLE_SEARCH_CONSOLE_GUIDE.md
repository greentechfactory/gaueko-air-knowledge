# Guía de Configuración de Google Search Console - Gaueko Air

Esta guía te ayudará a configurar Google Search Console para gaueko.es y enviar el sitemap.xml para acelerar la indexación de las 300 preguntas del knowledge-base.

---

## 📋 ¿Qué es Google Search Console?

Google Search Console es una herramienta **gratuita** de Google que te permite:

- ✅ Monitorear cómo Google indexa tu sitio web
- ✅ Enviar sitemaps para acelerar la indexación
- ✅ Ver qué búsquedas llevan tráfico a tu web
- ✅ Detectar errores de indexación
- ✅ Mejorar el rendimiento en resultados de búsqueda

**Coste:** 100% gratuito, sin límites

---

## 🚀 Paso 1: Acceder a Google Search Console

1. **Ve a:** https://search.google.com/search-console

2. **Inicia sesión** con tu cuenta de Google (la que quieres usar para gestionar gaueko.es)

3. **Haz clic en "Start now"** o "Empezar ahora"

---

## 🏠 Paso 2: Agregar la Propiedad gaueko.es

### 2.1. Seleccionar Tipo de Propiedad

Verás dos opciones:

- **Dominio** (Recomendado para gaueko.es)
- **Prefijo de URL**

**Selecciona "Dominio"** y escribe: `gaueko.es`

### 2.2. Verificar la Propiedad

Google te pedirá que verifiques que eres el propietario del dominio. Hay varias opciones:

#### Opción A: Verificación DNS (Recomendada)

1. Google te mostrará un **registro TXT** que debes agregar a tu DNS
2. Copia el registro TXT (algo como: `google-site-verification=ABC123XYZ...`)
3. Ve al panel de control de tu proveedor de dominio (donde compraste gaueko.es)
4. Busca la sección **"DNS"** o **"Gestión de DNS"**
5. Agrega un nuevo registro:
   - **Tipo:** TXT
   - **Nombre/Host:** @ (o déjalo vacío)
   - **Valor:** Pega el código que te dio Google
   - **TTL:** 3600 (o el valor por defecto)
6. **Guarda los cambios**
7. Vuelve a Google Search Console y haz clic en **"Verificar"**

⚠️ **Nota:** La verificación DNS puede tardar hasta 24-48 horas en propagarse, pero normalmente es instantánea.

#### Opción B: Archivo HTML (Más rápida si tienes acceso al servidor)

1. Google te dará un archivo HTML para descargar (ejemplo: `google1234567890abcdef.html`)
2. **Descarga el archivo**
3. **Sube el archivo a la raíz de tu sitio web:**
   - Si usas el servidor de Gaueko Air, sube el archivo a `/home/ubuntu/gaueko_air_web/client/public/`
   - El archivo debe ser accesible en: `https://gaueko.es/google1234567890abcdef.html`
4. Verifica que el archivo es accesible abriendo la URL en tu navegador
5. Vuelve a Google Search Console y haz clic en **"Verificar"**

#### Opción C: Etiqueta HTML (Si tienes acceso al código)

1. Google te dará una etiqueta meta como:
   ```html
   <meta name="google-site-verification" content="ABC123XYZ..." />
   ```
2. Copia la etiqueta
3. Agrégala al `<head>` de tu página principal
4. Vuelve a Google Search Console y haz clic en **"Verificar"**

---

## 📊 Paso 3: Enviar el Sitemap.xml

Una vez verificada la propiedad:

### 3.1. Acceder a la Sección de Sitemaps

1. En el menú lateral izquierdo, haz clic en **"Sitemaps"** (o "Mapas del sitio")
2. Verás un campo que dice **"Añadir un sitemap nuevo"**

### 3.2. Enviar el Sitemap

1. En el campo, escribe: `sitemap.xml`
2. Haz clic en **"Enviar"** o **"Submit"**

✅ **Listo!** Google comenzará a rastrear tu sitio usando el sitemap.

### 3.3. Verificar el Estado del Sitemap

Después de unos minutos (o hasta 24 horas), verás:

- **Estado:** Correcto ✅ (o "Success")
- **URLs descubiertas:** 4 (Home, FAQ, Knowledge Base, Sources)
- **Fecha del último rastreo**

---

## 📈 Paso 4: Monitorear la Indexación

### 4.1. Ver Páginas Indexadas

1. En el menú lateral, haz clic en **"Cobertura"** o **"Coverage"**
2. Aquí verás:
   - **Páginas válidas:** Cuántas páginas están indexadas
   - **Páginas excluidas:** Páginas que Google decidió no indexar
   - **Errores:** Problemas de indexación

### 4.2. Solicitar Indexación Manual (Opcional)

Para acelerar la indexación de páginas específicas:

1. En el menú superior, busca la barra de **"Inspeccionar cualquier URL"**
2. Escribe la URL completa, por ejemplo:
   - `https://gaueko.es/knowledge-base`
   - `https://gaueko.es/sources`
3. Haz clic en **Enter**
4. Si la página no está indexada, verás un botón **"Solicitar indexación"**
5. Haz clic y espera (puede tardar unos días)

---

## 🤖 Paso 5: Optimizar para IAs

### 5.1. Verificar que el Sitemap Incluye las Páginas Clave

El sitemap.xml ya incluye:

- ✅ `/` (Home) - Prioridad 1.0
- ✅ `/faq` (FAQ pública) - Prioridad 0.9
- ✅ `/knowledge-base` (300 preguntas) - Prioridad 0.95
- ✅ `/sources` (Referencias científicas) - Prioridad 0.85

### 5.2. Verificar robots.txt

El archivo `robots.txt` ya está configurado para permitir acceso a crawlers de IAs:

- GPTBot (ChatGPT)
- Claude-Web (Claude)
- PerplexityBot (Perplexity)
- Google-Extended (Gemini)

Puedes verificarlo en: https://gaueko.es/robots.txt

### 5.3. Monitorear Búsquedas

Después de unas semanas, podrás ver en **"Rendimiento"** (Performance):

- **Consultas:** Qué buscan los usuarios antes de llegar a tu web
- **Impresiones:** Cuántas veces aparece tu web en resultados de búsqueda
- **Clics:** Cuántas veces hacen clic en tu web
- **Posición media:** En qué posición apareces en los resultados

---

## 📊 Paso 6: Configurar Alertas por Email

Para recibir notificaciones de problemas:

1. Haz clic en el icono de **engranaje** (⚙️) en la esquina superior derecha
2. Selecciona **"Preferencias de Search Console"**
3. En **"Preferencias de correo electrónico"**, marca:
   - ☑️ **Todos los problemas de tu sitio**
   - ☑️ **Problemas de cobertura del índice**
   - ☑️ **Problemas de usabilidad móvil**
   - ☑️ **Problemas de seguridad**
4. Haz clic en **"Guardar"**

---

## 🎯 Resultados Esperados

### Primeras 24-48 horas:
- ✅ Sitemap procesado
- ✅ 4 URLs descubiertas
- ✅ Primeras páginas indexadas

### Primera semana:
- ✅ Todas las páginas indexadas (Home, FAQ, Knowledge Base, Sources)
- ✅ Primeras impresiones en resultados de búsqueda
- ✅ Datos de rendimiento disponibles

### Primer mes:
- ✅ Posicionamiento para términos clave:
  - "drones españa"
  - "fotogrametría grandes extensiones"
  - "gemelo digital drones"
  - "operadora UAS AESA"
  - "dragonfish españa"
- ✅ Tráfico orgánico creciente
- ✅ Indexación por IAs (ChatGPT, Claude, Perplexity)

---

## 🔄 Mantenimiento Continuo

### Semanal:
- Revisar **"Cobertura"** para detectar errores
- Verificar que no hay problemas de indexación

### Mensual:
- Analizar **"Rendimiento"** para ver qué búsquedas funcionan
- Optimizar contenido basándose en consultas reales
- Actualizar FAQ con nuevas preguntas basadas en búsquedas

### Trimestral:
- Comparar métricas con trimestre anterior
- Ajustar estrategia SEO según resultados
- Actualizar sitemap si se agregan nuevas páginas

---

## 📞 Soporte

Si tienes problemas durante la configuración:

- **Documentación oficial:** https://support.google.com/webmasters
- **Foro de ayuda:** https://support.google.com/webmasters/community
- **Email Gaueko Air:** air@gaueko.es

---

## ✅ Checklist de Configuración

- [ ] Acceder a Google Search Console
- [ ] Agregar propiedad gaueko.es
- [ ] Verificar propiedad (DNS, archivo HTML, o meta tag)
- [ ] Enviar sitemap.xml
- [ ] Solicitar indexación manual de /knowledge-base
- [ ] Solicitar indexación manual de /sources
- [ ] Configurar alertas por email
- [ ] Verificar que robots.txt es accesible
- [ ] Monitorear cobertura después de 24-48 horas
- [ ] Revisar rendimiento después de 1 semana

---

**Última actualización:** 29 de enero de 2025  
**Versión:** 1.0  
**Coste total:** 0€ (100% gratuito)
