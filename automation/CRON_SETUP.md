# Configuración de Actualización Automática Semanal

Este documento explica cómo configurar la actualización automática semanal del repositorio de conocimiento de Gaueko Air.

---

## 📅 Programación Recomendada

**Frecuencia:** Todos los lunes a las 09:00 AM

**Duración estimada:** 15-30 minutos

**Tareas automatizadas:**
1. Búsqueda de nuevos papers científicos en Google Scholar, arXiv, IEEE Xplore
2. Búsqueda de noticias del sector UAS (DroneDJ, sUAS News, etc.)
3. Actualización de estadísticas del repositorio
4. Generación de reporte semanal
5. Notificación por email (opcional)

---

## 🛠️ Configuración del Cron Job

### Opción 1: Configuración Manual

1. Abre el editor de crontab:
```bash
crontab -e
```

2. Añade la siguiente línea al final del archivo:
```bash
# Actualización semanal del repositorio Gaueko Air (todos los lunes a las 09:00)
0 9 * * 1 /home/ubuntu/gaueko_ai_repository/automation/weekly_update.sh
```

3. Guarda y cierra el editor (Ctrl+X, luego Y, luego Enter)

4. Verifica que el cron job se haya añadido correctamente:
```bash
crontab -l
```

### Opción 2: Configuración Automática

Ejecuta el siguiente comando:
```bash
(crontab -l 2>/dev/null; echo "0 9 * * 1 /home/ubuntu/gaueko_ai_repository/automation/weekly_update.sh") | crontab -
```

---

## 📝 Formato del Cron

```
┌───────────── minuto (0 - 59)
│ ┌───────────── hora (0 - 23)
│ │ ┌───────────── día del mes (1 - 31)
│ │ │ ┌───────────── mes (1 - 12)
│ │ │ │ ┌───────────── día de la semana (0 - 6) (0 = Domingo)
│ │ │ │ │
│ │ │ │ │
0 9 * * 1
```

**Ejemplos de programación:**

- **Todos los lunes a las 09:00:** `0 9 * * 1`
- **Todos los días a las 08:00:** `0 8 * * *`
- **Cada 6 horas:** `0 */6 * * *`
- **Primer día de cada mes a las 10:00:** `0 10 1 * *`

---

## 📊 Monitoreo de Ejecuciones

### Ver logs de ejecución

```bash
ls -lh /home/ubuntu/gaueko_ai_repository/logs/
```

### Ver el último log

```bash
tail -f /home/ubuntu/gaueko_ai_repository/logs/weekly_update_$(date '+%Y%m%d').log
```

### Ver reportes generados

```bash
ls -lh /home/ubuntu/gaueko_ai_repository/reports/
```

---

## 📧 Configuración de Notificaciones por Email (Opcional)

Para recibir notificaciones por email cuando se complete la actualización:

1. Instala `mailutils`:
```bash
sudo apt-get install mailutils
```

2. Configura tu servidor SMTP en `/etc/postfix/main.cf`

3. Crea el script de notificación:
```bash
nano /home/ubuntu/gaueko_ai_repository/automation/send_notification.py
```

4. Añade tu email en el script

---

## 🔧 Mantenimiento

### Desactivar actualización automática

```bash
crontab -e
# Comenta la línea añadiendo # al principio:
# 0 9 * * 1 /home/ubuntu/gaueko_ai_repository/automation/weekly_update.sh
```

### Ejecutar manualmente

```bash
/home/ubuntu/gaueko_ai_repository/automation/weekly_update.sh
```

### Verificar que el cron está corriendo

```bash
sudo service cron status
```

---

## ⚠️ Notas Importantes

1. **Permisos:** Asegúrate de que el script tiene permisos de ejecución (`chmod +x`)
2. **Rutas absolutas:** El cron job usa rutas absolutas para evitar problemas
3. **Logs:** Los logs se guardan automáticamente en `/home/ubuntu/gaueko_ai_repository/logs/`
4. **Espacio en disco:** Revisa periódicamente el espacio ocupado por los logs

---

## 📞 Soporte

Si tienes problemas con la configuración, contacta a:
- **Email:** air@gaueko.es
- **Teléfono:** +34 691 814 393

---

**Última actualización:** Noviembre 2025
