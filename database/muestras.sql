CREATE TABLE `muestras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pasos` int(11) ,
  `distancia` float(11) ,
  `calorias` float(11) ,
  `velocidad` float(11), 
  PRIMARY KEY  (`id`) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
 
--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `samples`
 
--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `samples`
--
ALTER TABLE `muestras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;