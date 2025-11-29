#!/bin/bash

# Script de actualización automática semanal para el repositorio de Gaueko Air
# Este script busca nuevos papers, noticias y actualizaciones del sector UAS

echo "🚀 Iniciando actualización semanal del repositorio Gaueko Air..."
echo "📅 Fecha: $(date '+%Y-%m-%d %H:%M:%S')"

# Directorio del repositorio
REPO_DIR="/home/ubuntu/gaueko_ai_repository"
LOG_FILE="$REPO_DIR/logs/weekly_update_$(date '+%Y%m%d').log"

# Crear directorio de logs si no existe
mkdir -p "$REPO_DIR/logs"

# Función para logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Iniciando actualización semanal"

# 1. Buscar nuevos papers científicos
log "🔍 Buscando nuevos papers científicos..."
python3 "$REPO_DIR/automation/search_papers.py" >> "$LOG_FILE" 2>&1

# 2. Buscar noticias del sector UAS
log "📰 Buscando noticias del sector UAS..."
python3 "$REPO_DIR/automation/search_news.py" >> "$LOG_FILE" 2>&1

# 3. Actualizar estadísticas
log "📊 Actualizando estadísticas..."
python3 "$REPO_DIR/automation/update_stats.py" >> "$LOG_FILE" 2>&1

# 4. Generar reporte semanal
log "📝 Generando reporte semanal..."
python3 "$REPO_DIR/automation/generate_report.py" >> "$LOG_FILE" 2>&1

# 5. Enviar notificación por email (opcional)
if [ -f "$REPO_DIR/automation/send_notification.py" ]; then
    log "📧 Enviando notificación..."
    python3 "$REPO_DIR/automation/send_notification.py" >> "$LOG_FILE" 2>&1
fi

log "✅ Actualización semanal completada"
echo ""
echo "📄 Log guardado en: $LOG_FILE"
echo "📊 Reporte disponible en: $REPO_DIR/reports/weekly_report_$(date '+%Y%m%d').md"
