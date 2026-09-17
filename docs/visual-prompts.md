# Recurso visual del perfil

## Ilustración de About me

- Archivo: `assets/about-astronaut.png`.
- Generado con la herramienta integrada `image_gen` como ilustración original de pixel art, con fondo transparente.
- La referencia del usuario orientó el formato: texto editable a la izquierda e ilustración aparte a la derecha.
- La ilustración no contiene la biografía; el texto se mantiene en el README para que pueda editarse y leerse con tecnologías de asistencia.

### Prompt del astronauta

```text
Use case: stylized-concept
Asset type: small original illustration placed beside the About me text in a minimal GitHub profile.
Primary request: a restrained monochrome pixel-art astronaut, shown from the waist up in three-quarter view facing slightly left toward the text. Large simple opaque dark visor, a compact life-support backpack, simplified suit geometry. Quiet, thoughtful, exploratory mood.
Style/medium: authentic low-resolution pixel art with clean hard square pixels, large readable shapes, very few details, about a 64-by-64-pixel design enlarged with nearest-neighbor style. No fine engraved texture and no realistic rendering.
Composition/framing: square image, one astronaut occupying about 78% of the canvas with generous transparent margins. Complete helmet and backpack inside frame, deliberate flat cropped waist.
Color palette: four neutral shades only: charcoal, medium gray, light gray, off-white. A dark outline and light silhouette edges should keep it legible on both white and dark webpage backgrounds.
Background: genuinely transparent alpha; no colored backdrop, no checkerboard baked in.
Constraints: no text, no letters, no flags, no badges, no logos, no stars, no planets, no floating particles, no motion trails, no glow, no gradients, no watermark. Original illustration, understated and legible at 170px wide.
```

## Halcón minimalista de estilo tech

- Archivo: `assets/falcon-minimal.png`.
- Generado con la herramienta integrada `image_gen`.
- El usuario pidió sustituir la primera propuesta de grabado realista por un símbolo tech con menos detalles.
- Se mantuvo la composición panorámica y se reemplazó el ave por una silueta geométrica, monocromática y de trazos amplios.
- La captura aportada se utilizó solo como referencia visual del perfil; no se reutilizaron su texto ni sus ilustraciones.
- `assets/profile-banner.jpg` y `assets/avatar.jpg` se conservan como recursos anteriores.

### Prompt final

```text
Use case: style-transfer
Asset type: minimal panoramic GitHub profile banner, 3:1 landscape.
Input image: the supplied falcon banner is the edit target. Preserve only the broad composition and dark background; completely replace the realistic engraved bird with a simple tech symbol.
Primary request: a very minimal geometric falcon emblem in flight facing right. It should read like a clean modern developer identity icon at a glance. Use just 4–6 bold, flat angular ivory shapes with precise negative-space cuts. Two swept-back angular wing shapes, a compact body and a small hooked beak are enough to communicate falcon. No individual feathers, no realistic anatomy rendering, no hatching, no stippling, no texture, no shading, no eye detail. Restrained original tech aesthetic, crisp vector-like edges, subtle asymmetry, elegant sharp geometry.
Scene/backdrop: perfectly flat solid #0d1117 charcoal, no texture, no gradient.
Composition: wide 3:1 horizontal canvas. One small emblem centered horizontally and vertically, occupying about 21% of canvas width and 43% of canvas height. Generous empty space all around. No decorative elements surrounding the emblem.
Color palette: only flat off-white #e6edf3 on charcoal.
Constraints: exactly one simple falcon symbol. No text, no circuit lines, no grids, no particles, no glow, no neon, no 3D, no realistic bird, no fine details, no border, no watermark. Produce the banner artwork itself.
```
