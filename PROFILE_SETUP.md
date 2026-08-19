# Cómo publicar este perfil

Todo lo necesario para la primera versión ya está en esta carpeta. El README usa el usuario público confirmado `israSanchezFal` y no publica tu correo académico.

## 1. Revisa el contenido

Abre `README.md` y confirma que las frases generales sí te representan. No añadí tecnologías, puesto profesional, proyectos destacados ni redes sociales porque todavía no tenemos esos datos.

## 2. Inicia sesión en GitHub CLI

La herramienta `gh` está instalada, pero no tiene una sesión activa:

```bash
gh auth login
```

Elige GitHub.com, HTTPS y el inicio de sesión desde el navegador.

## 3. Crea el repositorio especial del perfil

GitHub solo mostrará este README en tu perfil si el repositorio es público y se llama exactamente igual que tu usuario: `israSanchezFal`.

Desde esta carpeta, ejecuta:

```bash
git add README.md PROFILE_SETUP.md .gitignore docs assets
git commit -m "feat: create GitHub profile"
gh repo create israSanchezFal --public --source=. --remote=origin --push
```

Si el repositorio `israSanchezFal/israSanchezFal` ya existe, no vuelvas a crearlo. Conecta esta carpeta y sube los archivos:

```bash
git remote add origin https://github.com/israSanchezFal/israSanchezFal.git
git push -u origin main
```

## 4. Completa la columna izquierda del perfil

Esa parte no viene del README; se configura en GitHub con **Edit profile**.

- Sube `assets/avatar.jpg` como foto de perfil.
- Mantén `Israel Sanchez Falcon` como nombre visible si así quieres presentarte.
- Bio sugerida: `Developer in Mexico City — learning deeply, building thoughtfully, shipping consistently.`
- Conserva `Mexico City` como ubicación.
- Añade LinkedIn, portafolio o correo solo si quieres que sean públicos.
- Fija tus dos mejores repositorios desde **Customize your pins**.

## 5. Siguiente ronda de personalización

Para convertir esta base en un perfil realmente tuyo, faltan cinco datos:

1. Rol o especialidad.
2. Tecnologías que utilizas de verdad.
3. Dos a cuatro proyectos que quieras destacar.
4. LinkedIn, portafolio o canal de contacto público.
5. Si quieres el contenido final en inglés, español o bilingüe.

## Nota sobre las estadísticas

La tarjeta de estadísticas usa GitHub Readme Stats, un servicio externo. Si en algún momento falla, el resto del perfil seguirá funcionando y la gráfica nativa de contribuciones de GitHub seguirá visible.
