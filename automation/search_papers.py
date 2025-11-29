#!/usr/bin/env python3
"""
Script para buscar automáticamente papers científicos relevantes sobre UAS
y actualizar el repositorio de conocimiento de Gaueko Air.

Ejecutar semanalmente vía cron:
0 9 * * 1 /home/ubuntu/gaueko_ai_repository/automation/search_papers.py
"""

import requests
import json
from datetime import datetime, timedelta
import os

# Términos de búsqueda relevantes
SEARCH_TERMS = [
    "UAV photogrammetry",
    "drone digital twin",
    "BVLOS operations",
    "thermal imaging power lines",
    "multispectral agriculture drones",
    "UAS emergency response",
    "drone infrastructure monitoring",
    "RTK photogrammetry",
    "AI change detection drones",
    "forest fire monitoring UAV"
]

# APIs para búsqueda de papers
ARXIV_API = "http://export.arxiv.org/api/query"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_arxiv(query, max_results=5):
    """Busca papers en arXiv"""
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    try:
        response = requests.get(ARXIV_API, params=params, timeout=10)
        if response.status_code == 200:
            # Parse XML response (simplificado)
            papers = []
            # Aquí iría el parsing del XML de arXiv
            return papers
    except Exception as e:
        print(f"Error searching arXiv: {e}")
    
    return []

def search_semantic_scholar(query, max_results=5):
    """Busca papers en Semantic Scholar"""
    params = {
        'query': query,
        'limit': max_results,
        'fields': 'title,authors,year,abstract,url,citationCount'
    }
    
    try:
        response = requests.get(SEMANTIC_SCHOLAR_API, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
    except Exception as e:
        print(f"Error searching Semantic Scholar: {e}")
    
    return []

def save_findings(papers, output_file):
    """Guarda los hallazgos en un archivo Markdown"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Nuevos Papers Científicos - {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(f"**Última actualización:** {datetime.now().strftime('%d de %B de %Y')}\n\n")
        f.write("---\n\n")
        
        for term, results in papers.items():
            if results:
                f.write(f"## {term}\n\n")
                for paper in results:
                    f.write(f"### {paper.get('title', 'Sin título')}\n\n")
                    f.write(f"**Autores:** {', '.join([a.get('name', '') for a in paper.get('authors', [])])}\n\n")
                    f.write(f"**Año:** {paper.get('year', 'N/A')}\n\n")
                    f.write(f"**Citas:** {paper.get('citationCount', 0)}\n\n")
                    f.write(f"**Abstract:** {paper.get('abstract', 'No disponible')}\n\n")
                    f.write(f"**URL:** {paper.get('url', 'N/A')}\n\n")
                    f.write("---\n\n")

def main():
    """Función principal"""
    print(f"Iniciando búsqueda de papers - {datetime.now()}")
    
    all_papers = {}
    
    for term in SEARCH_TERMS:
        print(f"Buscando: {term}")
        papers = search_semantic_scholar(term, max_results=3)
        if papers:
            all_papers[term] = papers
            print(f"  Encontrados: {len(papers)} papers")
    
    # Guardar hallazgos
    output_dir = "/home/ubuntu/gaueko_ai_repository/research/weekly_updates"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(
        output_dir,
        f"papers_{datetime.now().strftime('%Y%m%d')}.md"
    )
    
    save_findings(all_papers, output_file)
    print(f"Hallazgos guardados en: {output_file}")
    
    # Crear notificación para revisión manual
    print("\n" + "="*50)
    print("ACCIÓN REQUERIDA:")
    print(f"Revisar nuevos papers en: {output_file}")
    print("Actualizar repositorio con hallazgos relevantes")
    print("="*50)

if __name__ == "__main__":
    main()
