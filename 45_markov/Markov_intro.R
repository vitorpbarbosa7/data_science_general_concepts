# matriz de adjacencia
# probabilidade de transicao

# origem nas linhas
# destino nas colunas

#  0        1       2
#0 0        1       0 
#1 0.25     0.5     0.25
#2 0.5      0.5     0


madj.data <- c(0,1,0,0.25,0.5,0.25,0.5,0.5,0)
madj = matrix(madj.data, nrow = 3, ncol = 3, byrow = TRUE)

madj2.data <- c(0,1,0, 0.05,0.9,0.05, 0.05,0.95,0)
madj2 = matrix(madj2.data, nrow = 3, ncol = 3, byrow = TRUE)

entropy_system = function(madj){
  
  epsilon = 1e-10
  madj = madj + epsilon
  
  # normalize
  M = t(apply(madj, 1, function(row) {row / sum(row) } ))
  
  entropies = M * log2(1/M)
  
  # uncertainty about the system
  sum_entropy = sum(entropies)
  
  return(sum_entropy)
  
}

e1 = entropy_system(madj)
e2 = entropy_system(madj2)

cat(e1)
cat(e2)






