# Perfil minimalista

El perfil está en `README.md`: un halcón geométrico, presentación, About me, Connect, Tech stack, GitHub stats y Activity graph. El contenido conserva el inglés del perfil anterior.

## Diseño

- `assets/falcon-minimal.png` es el banner actual: un halcón geométrico de estilo tech, sin detalles realistas y con espacio libre a su alrededor.
- Las secciones de la referencia se presentan con títulos sencillos y texto breve. El stack usa iconos oficiales de Devicon de 32 px, guardados en `assets/stack`, con el nombre de cada tecnología como texto alternativo y tooltip.
- El usuario confirmó Docker, Java, TypeScript, Python, Git, GitHub, PostgreSQL, MongoDB, Cassandra, Supabase y React. Se añadieron FastAPI y SQLAlchemy, verificados en `proyecto_final_sql`.
- Connect muestra iconos monocromáticos para GitHub, LinkedIn y correo. El correo público autorizado es `israsanchezf@icloud.com`. LinkedIn es un icono sin enlace, pendiente de que el usuario proporcione su URL.
- Las estadísticas y la gráfica son SVG locales en tonos neutros, generados con datos reales de GitHub. No dependen de un servicio externo de imágenes.
- La imagen es local y el texto usa el formato nativo de GitHub. El banner mantiene su fondo oscuro en ambos temas.
- `assets/profile-banner.jpg` y `assets/avatar.jpg` se conservan como recursos anteriores. El avatar de la cuenta se administra por separado en GitHub.
- El prompt del nuevo banner está documentado en `docs/visual-prompts.md`.

## Publicar una actualización

El remoto de esta carpeta apunta a `israSanchezFal/israSanchezFal`. El repositorio público con el mismo nombre que la cuenta es el que muestra el README en el perfil.

Si GitHub CLI necesita autenticación:

```bash
gh auth login -h github.com
```

Desde esta carpeta, revisa el cambio y publica únicamente los archivos del perfil:

```bash
git diff -- README.md PROFILE_SETUP.md docs/visual-prompts.md
git add README.md PROFILE_SETUP.md docs/visual-prompts.md assets/falcon-minimal.png assets/github-stats.svg assets/github-activity.svg assets/icons assets/stack scripts/render_profile.py scripts/profile.graphql .github/workflows/profile-stats.yml
git commit -m "Simplify GitHub profile design"
git push origin main
```

Los repositorios fijados y la gráfica de contribuciones nativa seguirán apareciendo en las secciones propias de GitHub.

## Actualización de estadísticas

`.github/workflows/profile-stats.yml` consulta la API GraphQL de GitHub y actualiza las dos tarjetas diariamente. También admite ejecución manual desde Actions. Utiliza el token automático del repositorio, sin secretos adicionales.

Las tarjetas muestran contribuciones y días activos del último año, repositorios públicos propios (sin forks) y contribuciones por semana. El periodo consultado queda visible. Los extremos de la gráfica pueden representar semanas parciales. Si la consulta falla, se conservan las últimas imágenes válidas.

Para regenerarlas manualmente desde la raíz del repositorio:

```bash
gh api graphql -f query="$(cat scripts/profile.graphql)" -f login=israSanchezFal > /tmp/isra-profile.json
python3 scripts/render_profile.py /tmp/isra-profile.json
```

La foto, bio lateral, logros y repositorios fijados son elementos de la cuenta de GitHub y no se cambian al publicar este README.
