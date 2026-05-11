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

## Paso 1 — Tests a pensar

### Funcionalidad 1: Add básico

| Test | Input | Expected |
|------|-------|----------|
| String vacío devuelve 0 | `Add("")` | `0` |
| Un número devuelve ese número | `Add("1")` | `1` |
| Dos números separados por coma | `Add("1,2")` | `3` |
