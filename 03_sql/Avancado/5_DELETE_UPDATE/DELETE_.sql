select * from filme


-- A forma segura de trabalhar com DML é com WHERE
delete from filme where filme_id = 5;

/*Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`ptskilla`.`filme_ator`, CONSTRAINT `fk_filme_ator_filme` FOREIGN KEY (`filme_id`) REFERENCES `filme` (`filme_id`) ON UPDATE CASCADE)
*/

-- Não deixou apagar porque filme_id também está presente como foreign key em filme ator
-- Logo precisamos primeiro deletar lá em filme_ator

delete from filme_ator where filme_id = 5;

delete from filme where filme_id = 5;

/* Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`ptskilla`.`filme_categoria`, CONSTRAINT `fk_filme_categoria_filme` FOREIGN KEY (`filme_id`) REFERENCES `filme` (`filme_id`) ON UPDATE CASCADE)
*/
delete from filme_categoria where filme_id = 5;

delete from filme where filme_id = 5;

/*Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`ptskilla`.`inventario`, CONSTRAINT `fk_inventario_filme` FOREIGN KEY (`filme_id`) REFERENCES `filme` (`filme_id`) ON UPDATE CASCADE)
*/

delete from inventario where filme_id = 5;

/*Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`ptskilla`.`aluguel`, CONSTRAINT `fk_aluguel_inventario` FOREIGN KEY (`inventario_id`) REFERENCES `inventario` (`inventario_id`) ON UPDATE CASCADE)
*/

-- Para não ficar tendo esses problemas, utilizar:
SET FOREIGN_KEY_CHECKS=0

delete from filme where filme_id = 5;
	