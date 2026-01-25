# Grid Collage 布局模板

**版本**: 1.0
**用途**: 多角度产品展示的网格拼贴布局
**参考**: 基于专业时尚摄影的9宫格框架

---

## 📐 支持的布局类型

### 3×3 Grid (9宫格) - 推荐

**适用场景**：
- 全方位产品展示
- 高端电商详情页
- 社交媒体轮播图
- 产品宣传海报

**特点**：
- 8格可见 + 1格中间遮挡 = 9格总数
- 中间3D产品巨大突出
- 最佳视觉冲击力

### 2×2 Grid (4宫格)

**适用场景**：
- 简洁对比展示
- 移动端优化
- 快速产品预览

**特点**：
- 4格全部可见或3格可见+1格遮挡
- 适合简约风格

### 4×1 Carousel (轮播条)

**适用场景**：
- 移动端横向滑动
- 产品细节展示
- 故事化叙事

**特点**：
- 横向4格排列
- 适合移动设备

---

## 🎨 3×3 Grid 完整框架（专业模板）

以下是用于生成9宫格产品摄影的完整提示词框架：

### 基础结构

```
Create a 2:3 portrait luxury product poster featuring THE SAME [PRODUCT] shown in 9 different product photography styles with 3D pop-out effect:
```

---

### PRODUCT CONSISTENCY (产品一致性规则)

**CRITICAL - HIGHEST PRIORITY**

THE SAME [产品类型] appears in ALL 9 positions:
- Same product model, same design, same brand
- [产品具体描述：材质、颜色、特征]
- [关键细节1]
- [关键细节2]
- [关键细节3]
- Its identity NEVER changes across all 9 appearances

**示例（手表）**：
```
THE SAME luxury timepiece appears in ALL 9 positions:
- Same watch model, same design, same brand
- Premium Swiss automatic watch with blue dial
- Stainless steel case with polished and brushed finish
- Blue sunburst dial with applied silver hour markers
- Date window at 3 o'clock position
- Steel bracelet with three-link design
- Sapphire crystal with anti-reflective coating
- Its identity NEVER changes across all 9 appearances
```

---

### BACKGROUND LAYER (Z=0) - 8格背景摄影

**Grid Structure & Occlusion:**
- Standard 3×3 layout = 9 product photography shots
- **8 visible cells** (center cell [2,2] COMPLETELY OCCLUDED by 3D product)
- Cells separated by DISTINCT THICK WHITE LINES (3-4px) for clear separation

**8个不同摄影角度定义**：

```
[1,1] Top View - [产品顶视角]:
- Same product, face-up/top-down perspective
- Style: Macro close-up of top details
- Lighting: Soft top light, minimal shadows
- Sharp focus, clear details

[1,2] [关键细节1] Detail:
- Same product, [具体角度]
- Style: Macro detail of [特定部位]
- Lighting: Rim light highlighting [材质]
- Sharp focus, clear details

[1,3] [关键细节2] Detail:
- Same product, [具体角度]
- Style: [拍摄风格]
- Lighting: Controlled reflection on [材质]
- Sharp focus, clear details

[2,1] 45-Degree Hero Angle:
- Same product, classic product photography angle
- Style: Editorial magazine presentation
- Lighting: Three-point lighting, elegant shadows
- Sharp focus, clear details

[2,3] [特殊角度] View:
- Same product, [具体描述]
- Style: [技术/艺术特点]
- Lighting: [光照方式]
- Sharp focus, clear details

[3,1] Lifestyle/Context Shot:
- Same product, in use or lifestyle context
- Style: [场景描述]
- Lighting: Natural elegant ambient light
- Sharp focus, clear details

[3,2] [材质/纹理] Detail:
- Same product, texture close-up
- Style: Macro focus on [材质细节]
- Lighting: Gradient light revealing texture
- Sharp focus, clear details

[3,3] Packaging/Presentation:
- Same product, in premium display/packaging
- Style: Unboxing luxury experience
- Lighting: Soft diffused light on presentation
- Sharp focus, clear details
```

**手表示例**：
- [1,1] Top View - Dial Detail（表盘俯视）
- [1,2] Crown & Case Side Detail（表冠侧面）
- [1,3] Clasp Mechanism Detail（表扣细节）
- [2,1] 45-Degree Hero Angle（经典45度角）
- [2,3] Case Back Exhibition（底盖/机芯）
- [3,1] On-Wrist Lifestyle Shot（上手效果）
- [3,2] Bracelet Link Detail（表带链节）
- [3,3] Packaging & Presentation（包装盒）

---

### CRITICAL TECHNICAL SPECS (背景网格技术规范)

- Deep depth of field (f/16) - ALL products sharp and clear
- NO bokeh, NO blur, NO out-of-focus areas
- Even bright studio lighting across all cells
- High resolution details in every cell
- Thick white grid lines clearly visible between cells
- Background color: Bright minimalist studio white/grey gradient

---

### FOREGROUND LAYER (Z=5-10cm forward) - 3D突出产品

**THE SAME [PRODUCT] (Center Dominant Presentation):**

- Massive hyper-realistic 3D rendered product dominating the center
- Positioned at EXACT CENTER, completely occluding center cell [2,2]
- **Product top touches very top edge of canvas**
- **Product bottom touches very bottom edge of canvas**
- Occupies MAXIMUM vertical space for strong 3D illusion

**Presentation Style:**
- Dynamic floating perspective with slight rotation
- [具体角度，如：30-degree tilt showing both front and side]
- Suspended in space, [无背景干扰]
- Direct frontal presentation, commanding presence
- Full product visible from top to bottom

**Technical Execution:**
- Product extends 5-10cm forward from background plane
- Hyper-realistic 3D render (Blender/Cinema 4D quality)
- Substance 3D material: [材质列表：polished metal, glass, leather等]
- +20% saturation compared to background for "pop forward" effect
- Slightly sharper focus than background (but background still sharp)
- Photorealistic reflections and refractions
- Visible [产品特征] clearly rendered

---

### OCCLUSION MECHANICS (遮挡机制)

**9格 - 1格遮挡 = 8格可见**

**Complete Occlusion:**
- Product body COMPLETELY covers center cell [2,2] (100% invisible)
- Center shot is fully hidden behind 3D product

**Partial Occlusion (Natural Edge Overlap):**
- Top [1,2]: [产品顶部] overlaps 10-15% into top detail shot
- Left [2,1]: [产品左侧] overlaps 15-20% into hero angle shot
- Right [2,3]: [产品右侧] overlaps 15-20% into right view shot
- Bottom [3,2]: [产品底部] overlaps 10-15% into bottom detail shot
- Overlaps break the white grid boundaries naturally

**Edge Treatment:**
- Soft organic transitions, NO hard cutout edges
- Product appears to physically exist in front of the grid
- Like a 3D display stand showcasing product above poster

---

### DEPTH EFFECTS (深度效果)

**Shadows:**
- Drop shadow from 3D product onto grid background
  * Blur: 12px
  * Color: rgba(0,0,0,0.25)
  * Offset: X=6px, Y=10px
- Contact shadow where product "hovers" on background
  * Blur: 8px
  * Color: rgba(0,0,0,0.35)
  * Creates floating suspension effect

**Lighting:**
- Background grid: Even bright studio lighting (no dramatic shadows)
- Foreground 3D product:
  * Key light upper left 45°
  * Fill light reducing harsh shadows
  * Rim light on edges for separation
  * Spotlight on key features for emphasis
- Consistent lighting direction across all elements

**Separation Techniques:**
- Slight brightness difference (foreground +10% brighter)
- Slight saturation boost (foreground +20% more saturated)
- Subtle sharpening halo around product edges
- Clear Z-axis spatial hierarchy

---

### CONSISTENCY RULES (一致性规则)

**Same Product Verification:**
- Same product model in all 9 positions
- Same [特征1] with identical [细节]
- Same [特征2] with same [细节]
- Same [特征3]
- Same [关键元素] position
- Same brand logo placement

**What Changes:**
- ✅ Photography style (macro, lifestyle, technical, editorial)
- ✅ Camera angle and perspective
- ✅ Lighting setup and mood
- ✅ Focal point (different details in each cell)

**What NEVER Changes:**
- ❌ The product model or brand
- ❌ The [核心特征1]
- ❌ The [核心特征2]
- ❌ Any product specifications

---

### TECHNICAL SPECIFICATIONS (技术规格)

**Image Composition:**
- Aspect ratio: 2:3 portrait (or 9:16 vertical)
- Resolution: 2000×3000 pixels (or higher)
- Color mode: RGB, sRGB color space
- Quality: Professional commercial product photography

**Camera & Focus:**
- **Deep depth of field (f/16 or higher)**
- **NO selective focus, NO bokeh, NO blur**
- **ALL products in background grid MUST be sharp and clear**
- Foreground product slightly sharper for hierarchy
- Both layers fully illuminated and visible

**Environment:**
- Bright minimalist indoor studio
- Pure white or soft grey gradient background
- Clean, uncluttered aesthetic
- Premium luxury brand presentation
- Museum-quality display mood

**Layout:**
- Background: Clear 3×3 grid with THICK WHITE LINES visible
- Foreground: Massive full-product 3D render breaking grid boundaries
- Surreal creative product collage composition
- Editorial luxury advertising feel

**Material Rendering (3D Product):**
[根据产品类型定制材质列表]
- [材质1]: [具体效果描述]
- [材质2]: [具体效果描述]
- [材质3]: [具体效果描述]

---

### FORBIDDEN ELEMENTS (严格禁止)

**Product:**
- ❌ Different product models in different cells
- ❌ Changing colors or designs
- ❌ Different brands or styles
- ❌ Inconsistent product details

**Technical:**
- ❌ Blurred background or bokeh effect
- ❌ Out of focus products in grid
- ❌ Shallow depth of field
- ❌ Missing or unclear grid lines
- ❌ Dark shadows obscuring details
- ❌ Low resolution or pixelation
- ❌ Deformed product shapes
- ❌ Messy composition

**Structure:**
- ❌ 4×4 or other grid sizes (must be 3×3)
- ❌ All 9 cells visible (center must be occluded)
- ❌ Flat composition (must have clear 3D depth)
- ❌ Hard cutout edges on foreground product

---

### QUALITY CHECKLIST (质量检查清单)

**Before Generation:**
- [ ] Same product model in all 9 positions?
- [ ] Each cell shows different photography style?
- [ ] Center cell [2,2] completely hidden?
- [ ] 8 visible background cells clearly defined?
- [ ] Thick white grid lines visible?
- [ ] ALL background products sharp and clear (no blur)?
- [ ] Foreground product full-size, top-to-bottom?
- [ ] Product extends maximum vertical space?
- [ ] Clear 3D pop-out effect with shadows?
- [ ] Natural edge overlaps into adjacent cells?
- [ ] Hyper-realistic 3D render quality?
- [ ] Deep depth of field maintained (f/16)?
- [ ] Material reflections realistic?
- [ ] Transparency/translucency visible (if applicable)?

---

### MIDJOURNEY COMMAND FORMAT

```
/imagine prompt: A surreal 3x3 luxury [product type] grid collage with THICK WHITE LINES separating cells. Background shows THE SAME [product description] in 8 different professional product photography styles ([列出8个角度]) - various angles but identical product. CENTER CELL HIDDEN. OVERLAID by a massive hyper-realistic 3D rendered floating version of THE SAME PRODUCT, top touching top edge, bottom touching bottom edge, [angle description]. ALL products in background sharp and in focus, deep depth of field f/16, no blur anywhere, bright studio lighting, clear white grid lines visible, strong 3D pop-out effect with drop shadows, professional commercial product photography, same product 9 times, photorealistic Substance 3D materials, [material list], 8k resolution --ar 2:3 --v 6.1 --style raw --quality 2
```

---

### MATHEMATICAL LOGIC (数学逻辑)

```
Same product × 9 different photography styles arranged in 3×3 grid.

Center style completely occluded by 3D foreground version =
8 visible background shots + 1 foreground 3D render =
9 total appearances of ONE PRODUCT with NINE photographic interpretations.
```

---

## 🎯 产品类型适配

### 手表 (Luxury Watch)

**8个角度**：
1. 表盘俯视 (Top View - Dial Detail)
2. 表冠侧面 (Crown & Case Side Detail)
3. 表扣细节 (Clasp Mechanism Detail)
4. 经典45度角 (45-Degree Hero Angle)
5. 底盖/机芯 (Case Back Exhibition)
6. 上手效果 (On-Wrist Lifestyle Shot)
7. 表带链节 (Bracelet Link Detail)
8. 包装盒 (Packaging & Presentation)

**材质渲染**：
- Polished stainless steel: mirror reflections
- Brushed steel: subtle linear grain
- Sapphire crystal: transparent with refraction
- Leather strap: realistic texture and stitching

### 香水 (Perfume Bottle)

**8个角度**：
1. 瓶盖俯视 (Cap Top View)
2. 瓶身侧面 (Bottle Side Profile)
3. 品牌Logo特写 (Brand Logo Detail)
4. 经典45度角 (45-Degree Hero Angle)
5. 瓶底设计 (Base Design Detail)
6. 使用场景 (Lifestyle Context Shot)
7. 液体/渐变 (Liquid Gradient Detail)
8. 包装盒 (Luxury Box Presentation)

**材质渲染**：
- Glass bottle: transparency, light refraction
- Gold cap: metallic sheen
- Liquid: color gradient, translucency
- Embossed logo: subtle depth

### 电子产品 (Electronics)

**8个角度**：
1. 正面屏幕 (Front Screen View)
2. 侧面端口 (Side Ports Detail)
3. 背面Logo (Back Logo & Design)
4. 经典45度角 (45-Degree Hero Angle)
5. 内部结构 (Internal Structure/Components)
6. 使用场景 (In-Use Lifestyle Shot)
7. 材质纹理 (Material Texture Close-up)
8. 包装全家福 (Unboxing All Contents)

**材质渲染**：
- Aluminum body: brushed metal finish
- Glass screen: anti-glare coating
- Plastic: matte or glossy finish
- LED indicators: subtle glow

---

## 💡 使用建议

1. **选择合适的产品角度**：根据产品特点选择最能展示特征的8个角度
2. **保持一致性**：所有9个位置必须是同一产品
3. **材质真实性**：3D渲染的材质要与实物照片一致
4. **光照统一**：背景8格用均匀光照，前景3D用戏剧性光照
5. **深景深必须**：f/16确保所有格子都清晰，避免bokeh

---

**最后更新**: 2026-01-04
**维护者**: Product Master Skill System
