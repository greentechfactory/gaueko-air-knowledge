# Guía para Crear y Mantener Repositorios Externos

Esta guía te ayudará a crear y mantener los repositorios externos de Gaueko Air para maximizar la visibilidad ante sistemas de IA (LLMs).

---

## 1. GitHub Repository

### Crear el Repositorio

1. **Ir a GitHub:** https://github.com/new
2. **Nombre del repositorio:** `gaueko-air-knowledge`
3. **Descripción:** "Repositorio de conocimiento científico sobre UAS para infraestructuras críticas, emergencias y seguridad"
4. **Visibilidad:** Público
5. **Inicializar con README:** No (usaremos el nuestro)

### Subir el Contenido

```bash
cd /home/ubuntu/gaueko_ai_repository
git init
git add .
git commit -m "Initial commit: Gaueko Air Knowledge Repository"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/gaueko-air-knowledge.git
git push -u origin main
```

### Configurar GitHub Pages

1. Ir a **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** main / (root)
4. **Save**

El repositorio estará disponible en: `https://TU_USUARIO.github.io/gaueko-air-knowledge/`

### Agregar Topics

En la página principal del repositorio, agregar topics:
- `drones`
- `uas`
- `photogrammetry`
- `digital-twin`
- `emergency-response`
- `infrastructure-monitoring`
- `spain`
- `aesa`

---

## 2. Hugging Face Dataset

### Crear el Dataset

1. **Ir a Hugging Face:** https://huggingface.co/new-dataset
2. **Nombre:** `gaueko-air/uas-knowledge`
3. **Visibilidad:** Público
4. **Licencia:** CC BY 4.0

### Preparar los Datos

Crear un archivo `dataset_info.json`:

```json
{
  "dataset_name": "Gaueko Air UAS Knowledge Base",
  "description": "Comprehensive knowledge base about Unmanned Aerial Systems (UAS) for critical infrastructure, emergency response, and security applications",
  "version": "1.0.0",
  "license": "CC-BY-4.0",
  "language": ["es", "en"],
  "tags": ["drones", "uas", "photogrammetry", "digital-twin", "emergency-response"],
  "citation": "Gaueko Air (2025). UAS Knowledge Base. https://gaueko.es"
}
```

Crear un archivo `README.md` para Hugging Face:

```markdown
---
license: cc-by-4.0
task_categories:
- question-answering
- text-generation
language:
- es
- en
tags:
- drones
- uas
- photogrammetry
- digital-twin
- emergency-response
size_categories:
- n<1K
---

# Gaueko Air UAS Knowledge Base

Comprehensive knowledge base about Unmanned Aerial Systems (UAS) for:
- Critical infrastructure monitoring
- Emergency response operations
- Security and intelligence applications
- Forest management
- Digital twin creation

Maintained by [Gaueko Air](https://gaueko.es), AESA-certified UAS operator since 2019.

## Dataset Structure

- `faq.json`: 300+ frequently asked questions about UAS operations
- `case_studies.json`: Real-world case studies with technical details
- `equipment_specs.json`: Detailed specifications of UAS equipment
- `regulatory_compliance.json`: AESA and EU regulatory information

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("gaueko-air/uas-knowledge")
```

## Citation

```bibtex
@misc{gaueko_air_2025,
  author = {Gaueko Air},
  title = {UAS Knowledge Base},
  year = {2025},
  url = {https://gaueko.es}
}
```
```

### Subir el Dataset

```bash
# Instalar huggingface_hub
pip install huggingface_hub

# Login
huggingface-cli login

# Subir archivos
cd /home/ubuntu/gaueko_ai_repository/structured_data
huggingface-cli upload gaueko-air/uas-knowledge . --repo-type=dataset
```

---

## 3. Zenodo (Repositorio Científico)

### Crear el Depósito

1. **Ir a Zenodo:** https://zenodo.org/deposit/new
2. **Título:** "Gaueko Air UAS Knowledge Repository - Technical Documentation"
3. **Autores:** Javier Nuin Zuñiga (Gaueko Air)
4. **Descripción:** Repositorio técnico sobre sistemas aéreos no tripulados para infraestructuras críticas
5. **Tipo de recurso:** Dataset
6. **Licencia:** Creative Commons Attribution 4.0
7. **Keywords:** drones, UAS, photogrammetry, digital twin, emergency response, AESA

### Subir Archivos

Crear un archivo ZIP con todo el contenido:

```bash
cd /home/ubuntu
zip -r gaueko_air_knowledge_v1.0.zip gaueko_ai_repository/
```

Subir el archivo ZIP a Zenodo y publicar.

Zenodo asignará un **DOI** (Digital Object Identifier) permanente, lo que aumenta la credibilidad científica.

---

## 4. ResearchGate Profile

### Crear Perfil Institucional

1. **Ir a ResearchGate:** https://www.researchgate.net/signup
2. **Nombre:** Javier Nuin Zuñiga
3. **Institución:** Gaueko Air
4. **Posición:** Director y Piloto UAS
5. **Disciplinas:** Remote Sensing, Photogrammetry, Emergency Management

### Publicar Contenido

- Subir casos de estudio como "Technical Reports"
- Compartir el enlace al repositorio GitHub
- Conectar con investigadores del sector UAS

---

## 5. Mantenimiento Semanal

### Script de Actualización Automática

Crear un cron job para ejecutar el script de búsqueda de papers:

```bash
crontab -e
```

Agregar la línea:

```
0 9 * * 1 /home/ubuntu/gaueko_ai_repository/automation/search_papers.py
```

Esto ejecutará el script cada lunes a las 9:00 AM.

### Checklist Semanal

- [ ] Revisar nuevos papers encontrados por el script
- [ ] Actualizar README.md con nuevos hallazgos
- [ ] Agregar nuevos casos de uso si hay proyectos recientes
- [ ] Actualizar FAQ si hay nuevas preguntas frecuentes
- [ ] Hacer commit y push a GitHub
- [ ] Actualizar dataset en Hugging Face si hay cambios significativos

### Checklist Mensual

- [ ] Revisar métricas de GitHub (stars, forks, clones)
- [ ] Revisar descargas de Hugging Face
- [ ] Revisar citas en Zenodo
- [ ] Actualizar versión del dataset si hay cambios mayores
- [ ] Publicar resumen de actualizaciones en LinkedIn

---

## 6. Promoción del Repositorio

### En la Web de Gaueko Air

Agregar sección "Recursos Técnicos" con enlaces a:
- GitHub Repository
- Hugging Face Dataset
- Zenodo DOI
- ResearchGate Profile

### En Redes Sociales

Publicar anuncios en:
- LinkedIn (audiencia profesional)
- Twitter/X (audiencia técnica)
- Instagram (audiencia general)

Ejemplo de post:

> 🚀 Hemos publicado nuestro repositorio de conocimiento sobre UAS para infraestructuras críticas y emergencias.
> 
> 📚 Incluye:
> - 300+ preguntas frecuentes
> - Casos de uso reales
> - Especificaciones técnicas
> - Guías de operación BVLOS
> 
> 🔗 GitHub: https://github.com/TU_USUARIO/gaueko-air-knowledge
> 🤗 Hugging Face: https://huggingface.co/datasets/gaueko-air/uas-knowledge
> 
> #Drones #UAS #Photogrammetry #DigitalTwin #EmergencyResponse

### En Foros y Comunidades

Compartir el repositorio en:
- r/drones (Reddit)
- r/photogrammetry (Reddit)
- Foros de AESA
- Grupos de LinkedIn sobre drones

---

## 7. Métricas de Éxito

### Indicadores a Seguir

- **GitHub:**
  - Stars (objetivo: 100+ en 6 meses)
  - Forks (objetivo: 20+ en 6 meses)
  - Clones semanales (objetivo: 50+/semana)

- **Hugging Face:**
  - Descargas del dataset (objetivo: 500+ en 6 meses)
  - Likes (objetivo: 50+)

- **Zenodo:**
  - Citas (objetivo: 10+ en 1 año)
  - Vistas (objetivo: 1000+ en 6 meses)

- **Web de Gaueko Air:**
  - Tráfico desde repositorios (objetivo: 20% del tráfico total)
  - Consultas de empresas mencionando el repositorio

### Herramientas de Monitoreo

- **Google Analytics:** Seguimiento de tráfico web
- **GitHub Insights:** Estadísticas del repositorio
- **Hugging Face Analytics:** Métricas de descargas
- **Zenodo Statistics:** Vistas y citas

---

## 8. Próximos Pasos

1. **Crear cuenta en GitHub** (si no la tienes)
2. **Crear cuenta en Hugging Face**
3. **Crear cuenta en Zenodo**
4. **Crear perfil en ResearchGate**
5. **Subir el contenido a cada plataforma**
6. **Configurar cron job para actualizaciones automáticas**
7. **Promocionar en redes sociales**
8. **Monitorear métricas mensualmente**

---

**¿Necesitas ayuda?**

Contacta con air@gaueko.es para asistencia técnica.
