CREATE TABLE `fornecedor` (
`fornecedor_id` smallint (5) unsigned not null auto_increment,
`primeiro_nome` varchar (45) not null, 
`ultimo_nome` varchar (45) not null,
`email` varchar (50) default null,
`ativo` tinyint (1) not null default '1', 
`data_criacao` datetime not null, 
`ultima_atualizacao` timestamp not null default current_timestamp on update current_timestamp,
PRIMARY KEY (`fornecedor_id`)
) ENGINE = InnoDB AUTO_INCREMENT=600 DEFAULT CHARSET=utf8

select * 
from fornecedor
