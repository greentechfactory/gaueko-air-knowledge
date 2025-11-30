#!/bin/bash

# Script de publicación del repositorio Gaueko Air Knowledge en GitHub
# Autor: Gaueko Air
# Fecha: 29 de enero de 2025

echo "=============================================="
echo "  Publicación de Gaueko Air Knowledge Repo"
echo "=============================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "README.md" ]; then
    echo "❌ Error: Ejecuta este script desde /home/ubuntu/gaueko_ai_repository"
    exit 1
fi

# Verificar que Git está configurado
if [ ! -d ".git" ]; then
    echo "❌ Error: No se encontró repositorio Git. Ejecuta primero: git init"
    exit 1
fi

echo "📋 Paso 1: Crear el repositorio en GitHub manualmente"
echo ""
echo "Ve a: https://github.com/new"
echo ""
echo "Configuración del repositorio:"
echo "  - Repository name: gaueko-air-knowledge"
echo "  - Description: Repositorio de conocimiento científico sobre UAS para infraestructuras críticas, emergencias y seguridad. AI-Friendly content con 300+ Q&A estructuradas."
echo "  - Visibility: ✅ Public"
echo "  - ❌ NO marques 'Initialize this repository with a README'"
echo "  - ❌ NO agregues .gitignore"
echo "  - ❌ NO agregues licencia (ya está incluida)"
echo ""
read -p "¿Has creado el repositorio en GitHub? (s/n): " created

if [ "$created" != "s" ]; then
    echo "❌ Cancelado. Crea el repositorio primero."
    exit 1
fi

echo ""
echo "📋 Paso 2: Conectar repositorio local con GitHub"
echo ""

# Solicitar nombre de usuario
read -p "Introduce tu nombre de usuario de GitHub: " username

# Agregar remote origin
git remote remove origin 2>/dev/null
git remote add origin "https://github.com/$username/gaueko-air-knowledge.git"

echo "✅ Remote configurado: https://github.com/$username/gaueko-air-knowledge.git"
echo ""

echo "📋 Paso 3: Subir código a GitHub"
echo ""

# Cambiar a rama main
git branch -M main

# Push
echo "Subiendo archivos a GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=============================================="
    echo "  ✅ ¡Repositorio publicado exitosamente!"
    echo "=============================================="
    echo ""
    echo "🔗 URL del repositorio:"
    echo "   https://github.com/$username/gaueko-air-knowledge"
    echo ""
    echo "📋 Próximos pasos:"
    echo ""
    echo "1. Configura los Topics del repositorio:"
    echo "   - Ve a: https://github.com/$username/gaueko-air-knowledge"
    echo "   - Haz clic en el icono de engranaje (⚙️) junto a 'About'"
    echo "   - Agrega estos topics:"
    echo "     uas, drones, photogrammetry, digital-twin, ai-friendly,"
    echo "     emergency-response, critical-infrastructure, aesa, spain,"
    echo "     knowledge-base, faq, structured-data, json-ld"
    echo ""
    echo "2. Verifica que el README se muestra correctamente con los badges"
    echo ""
    echo "3. Opcional: Activa GitHub Pages en Settings → Pages"
    echo ""
else
    echo ""
    echo "❌ Error al subir el repositorio."
    echo ""
    echo "Si pide credenciales:"
    echo "  - Usuario: $username"
    echo "  - Contraseña: Usa tu Personal Access Token (no tu contraseña de GitHub)"
    echo ""
    echo "Para crear un token:"
    echo "  1. Ve a: https://github.com/settings/tokens"
    echo "  2. Generate new token (classic)"
    echo "  3. Marca: repo"
    echo "  4. Copia el token y úsalo como contraseña"
    echo ""
fi
