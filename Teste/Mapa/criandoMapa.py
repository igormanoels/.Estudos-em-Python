
import folium

# Criar o mapa
mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=13)

# Adicionar um marcador
folium.Marker(
    location=[-23.5505, -46.6333],
    popup='São Paulo',
    tooltip='Clique para mais info'
).add_to(mapa)

# Salvar em HTML
mapa.save('meu_mapa.html')

print("Mapa salvo como 'meu_mapa.html'. Abra no navegador para visualizar.")
