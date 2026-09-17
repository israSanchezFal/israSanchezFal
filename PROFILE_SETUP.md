# Perfil minimalista

El perfil está en `README.md`: un halcón geométrico, presentación, About me, Connect y Tech stack. El contenido conserva el inglés del perfil anterior y termina después de los iconos del stack.

## Diseño

- `assets/falcon-minimal.png` es el banner actual: un halcón geométrico de estilo tech, sin detalles realistas y con espacio libre a su alrededor.
- Las secciones de la referencia se presentan con títulos sencillos y texto breve. El stack usa iconos oficiales de Devicon de 32 px, guardados en `assets/stack`, con el nombre de cada tecnología como texto alternativo y tooltip.
- El usuario confirmó Docker, Java, TypeScript, Python, Git, GitHub, PostgreSQL, MongoDB, Cassandra, Supabase y React. Se añadieron FastAPI y SQLAlchemy, verificados en `proyecto_final_sql`.
- Connect muestra iconos monocromáticos para GitHub, LinkedIn y correo. El correo público autorizado es `israsanchezf@icloud.com`. LinkedIn es un icono sin enlace, pendiente de que el usuario proporcione su URL.
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
git add README.md PROFILE_SETUP.md docs/visual-prompts.md assets/falcon-minimal.png assets/icons assets/stack
git commit -m "Simplify GitHub profile design"
git push origin main
```

Los repositorios fijados y la gráfica de contribuciones nativa seguirán apareciendo en las secciones propias de GitHub.

La foto, bio lateral, logros y repositorios fijados son elementos de la cuenta de GitHub y no se cambian al publicar este README.
