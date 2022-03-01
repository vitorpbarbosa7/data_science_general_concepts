# Adicionar coluna com ALTER TABLE ADD COLUMNS

ALTER TABLE `ptskilla`.`fornecedor`
ADD COLUMN `confiavel` tinyint(1) null after `ultima_atualizacao`;