## CSS Color Variables

```css
:root {
  /* Image Palette Colors */
  --color-cream: #FDF0D5;
  --color-deep-navy: #003049;
  --color-maroon: #780000;
  --color-crimson: #C1121F;
  --color-sky-blue: #669BBC;

  /* Usage Mapping */
  --form-background: #FDF0D5;
  --form-text: #003049;

  --input-border: #669BBC;
  --input-focus-border: #C1121F;
  --input-focus-bg: #fff6df;

  --button-gradient-start: #780000;
  --button-gradient-end: #C1121F;
  --button-text: #FDF0D5;

  --background-gradient: linear-gradient(
    135deg,
    #003049 0%,
    #780000 40%,
    #C1121F 70%,
    #669BBC 100%
  );

  --helper-text: #003049;
  --box-shadow: 0 10px 30px rgba(0, 48, 73, 0.35);
}
```

---

## Component Styling Reference

### Login Form Box
```css
.box {
    background: var(--form-background);
    border-radius: 15px;
    box-shadow: var(--box-shadow);
}
```

### Input Fields
```css
.box input[type="text"],
.box input[type="password"] {
    border: 2px solid var(--input-border);
    color: var(--form-text);
    background: #ffffff;
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
    border-color: var(--input-focus-border);
    background-color: var(--input-focus-bg);
}
```

### Submit Button
```css
.box input[type="submit"] {
    background: linear-gradient(
        135deg,
        var(--button-gradient-start),
        var(--button-gradient-end)
    );
    color: var(--button-text);
    border: 2px solid var(--button-gradient-start);
    transition: 0.3s ease;
}

.box input[type="submit"]:hover {
    background: linear-gradient(
        135deg,
        var(--button-gradient-end),
        var(--button-gradient-start)
    );
    transform: scale(1.05);
}
```

### Background Gradient
```css
body {
    background: var(--background-gradient);
    min-height: 100vh;
}
```