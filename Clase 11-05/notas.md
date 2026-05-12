# Ciclo TDD

**Red → Green → Refactor**

1. **Red**: escribir un test que falla
2. **Green**: escribir el código mínimo para que el test pase
3. **Refactor**: mejorar el código sin romper los tests

---

# String Calculator Kata

## Metodología

- Pensar los Tests que van a codear
- Codear un Test a la vez
- Cuando se termina un Test lo suben al repositorio
- Cambian de Programador
- Siguen por otro Test
- Cuando están todos los Tests listos para una funcionalidad avisar para seguir con la siguiente

---

## Tests — String Calculator

| # | Descripción | Input | Expected |
|---|-------------|-------|----------|
| 1 | String vacío devuelve 0 | `Add("")` | `0` |
| 2 | Un número devuelve ese número | `Add("1")` | `1` |
| 3 | Dos números separados por coma | `Add("1,2")` | `3` |
| 4 | Múltiples números | `Add("1,2,3")` | `6` |
| 5 | Salto de línea como separador | `Add("1\n2")` | `3` |
| 6 | Mezcla de coma y salto de línea | `Add("1\n2,3")` | `6` |


| 7 | Un negativo solo lanza excepción | `Add("-1")` | Exception: `"negatives not allowed: -1"` |
| 8 | Negativo entre positivos lanza excepción | `Add("1,-2,3")` | Exception: `"negatives not allowed: -2"` |
| 9 | Múltiples negativos en la excepción | `Add("-1,-2,3")` | Exception: `"negatives not allowed: -1, -2"` |
| 10 | Solo negativos | `Add("-1,-2")` | Exception: `"negatives not allowed: -1, -2"` |
| 11 | Negativo con salto de línea | `Add("1\n-2,3")` | Exception: `"negatives not allowed: -2"` |
| 12 | Mezcla de separadores con varios números | `Add("1\n2,3\n4")` | `10` |
