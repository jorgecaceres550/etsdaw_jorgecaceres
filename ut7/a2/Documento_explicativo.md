# UT7A2 – Informe de Refactorización de Código

### Análisis y Mejora del Código

En primer lugar, se aplicó la técnica de **Rename Variable** para sustituir identificadores por nombres descriptivos, mejorando la coherencia y legibilidad del código. Posteriormente, se eliminaron los **"números mágicos"** mediante la sustitución por constantes, facilitando el mantenimiento futuro.

Siguiendo el **principio de responsabilidad única**, se redistribuyeron las tareas mediante la técnica de **Extract Method**, delegando en la clase **Producto** el cálculo de su propio subtotal a través de una **property** y creando una nueva clase denominada **Carrito** para encapsular la gestión global de la compra.

Finalmente, se optimizó la lógica de presentación implementando el método mágico **__repr__** mejorando la lectura del producto en sí; por otro lado, logramos desacoplar la lógica de cálculo de la salida por consola, resultando en un programa limpio, escalable y con una estructura que garantiza una evolución técnica eficiente.

---

### Fundamentos Aplicados

Esta guía fue creada a partir de los principios **SOLID**:
- **Responsabilidad única**
- **Abierto/Cerrado**
- **Sustitución de Liskov**
- **Segregación de interfaz**
- **Inversión de dependencias**

