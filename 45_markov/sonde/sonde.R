# reference https://www.researchgate.net/publication/220998673_A_self-organizing_neural_network_for_detecting_novelties

entropy = function(markov){
  entropy_calc = sum(markov * log2(1/markov))
  return (entropy_calc)
}


get_closest_centroid = function(example, centroids, sigma, threshold=1e-3){
  #' Retorna qual o centroid mais proximo em relacao a um unico ponto, avaliando para diferentes 
  #' centroides disponiveis
  
  # espaco ainda sem gaussianas
  if (is.null(centroids))
    return (-1)
  
  # distancia euclidiana do exemplo para o centroid
  E = apply(centroids, 1, function(center) {dist(center, example)})
  #cat('Distance',E,'\n')
  
  # ativacao da gaussian em relacao a cada ponto
  # esta collection vai ter exatamente o numero de centroids
  activation = exp(-E^2 / (2*sigma^2))
  #cat('Activation',activation,'\n')
  # reference https://www.researchgate.net/publication/220998673_A_self-organizing_neural_network_for_detecting_novelties
  
  get_closest_centroid = function(example, centroids, sigma, threshold=1e-3){
    #' Retorna qual o centroid mais proximo em relacao a um unico ponto, avaliando para diferentes 
    #' centroides disponiveis
    
    # espaco ainda sem gaussianas
    if (is.null(centroids))
      return (-1)
    
    # distancia euclidiana do exemplo para o centroid
    E = apply(centroids, 1, function(center) {dist(center, example)})
    #cat('Distance',E,'\n')
    
    # ativacao da gaussian em relacao a cada ponto
    # esta collection vai ter exatamente o numero de centroids
    activation = exp(-E^2 / (2*sigma^2))
    #cat('Activation',activation,'\n')
    
    # qual gaussiana com maior ativacao (goodness of fitness)
    id = which.max(activation)
    
    activation[id] > threshold
    
    # se a ativacao for menor que o threhold, criamos uma nova gaussiana
    if (activation[id] < threshold)
      return (-1)
    
    # retornar a posicao, o id, do centroid mais proximo deste ponto, deste exemplo que foi passado
    return (id)
  }
  
  dist = function(point_a, point_b){
    distance = sqrt(sum((point_a - point_b)**2))
    return (distance)
  }
  
  sonde = function(X, alpha=0.01, sigma=1,eps=1e-7,delta=0.01){
    
    if (!is.data.frame(X)) {
      return ("X must be dataframe")
    }
    
    # precisamos inicializar?
    centroids = NULL
    old_position = -1
    current_position = -1
    markov = NULL
    
    for (i in 1:nrow(X)) {
      example = X[i,]
      current_position = get_closest_centroid(example, centroids, sigma)
      if (current_position == -1) {
        # Criar uma gaussiana para representar novo exemplo
        
        # ou sejsa, uma criacao de centroids sob demanda, adorei o termo
        centroids = rbind(centroids, example)
        
        # Atual posicao, estado, eh no ultimo centroide criado nesta condicional
        current_position = nrow(centroids)
        
        # MARKOV CHAIN IMPLEMENTATION
        markov = rbind(markov,eps)
        
        if (nrow(centroids) > 1)
          markov = cbind(markov,eps)
        
        # delta representa a visita, quando um estado eh visitado
        
        # matriz de adjacencia
        #                 to
        #             [,1]      [,2]
        # from [1,]   1e-7+delta  1e-7   --> 1000/1001    1/1001 
        #      [2,]   1e-7  1e-7
        
        
        # print("centroids")
        # print(centroids)
      }
      # se nao criamos um centroide, vamos adaptar a Gaussiana visitada
      else {
        # media movel exponencialmente ponderada
        # combinacao linear simples do atual centro e do novo ponto 
        centroids[current_position,] = (1-alpha)*centroids[current_position,] + alpha*example
      }
      
      if (old_position != -1){
        # visitei alguem
        print(paste("from: ", old_position, " to: ", current_position))
        
        #markov[from, to]
        markov[old_position, current_position] = markov[old_position, current_position] + delta
        
        # cada linha da matriz de adjacencia deve somar 1, para representar uma probabilidade a transicao 
        # para cada estado destino a partir de um esatdo origem
        for (j in 1:nrow(markov)){
          markov[j,] = markov[j,] / sum(markov[j,])
        }
      }
      
      print('Adjacency Matrix')
      print(markov)
      
      
      # atualizar a posicao, que foi transicionada 
      old_position = current_position
    }
  }
  
  X = read.table('dataset.dat')
  sonde(X)
  
  
  
  
  
  
  # qual gaussiana com maior ativacao (goodness of fitness)
  id = which.max(activation)
  
  activation[id] > threshold
  
  # se a ativacao for menor que o threhold, criamos uma nova gaussiana
  if (activation[id] < threshold)
    return (-1)
  
  # retornar a posicao, o id, do centroid mais proximo deste ponto, deste exemplo que foi passado
  return (id)
}

dist = function(point_a, point_b){
  distance = sqrt(sum((point_a - point_b)**2))
  return (distance)
}

sonde = function(X, alpha=0.01, sigma=1,eps=1e-7,delta=0.01){
  
  if (!is.data.frame(X)) {
    return ("X must be dataframe")
  }
  
  # precisamos inicializar?
  centroids = NULL
  old_position = -1
  current_position = -1
  markov = NULL
  
  for (i in 1:nrow(X)) {
    example = X[i,]
    current_position = get_closest_centroid(example, centroids, sigma)
    if (current_position == -1) {
      # Criar uma gaussiana para representar novo exemplo
      
      # ou sejsa, uma criacao de centroids sob demanda, adorei o termo
      centroids = rbind(centroids, example)
      
      # Atual posicao, estado, eh no ultimo centroide criado nesta condicional
      current_position = nrow(centroids)
      
      # MARKOV CHAIN IMPLEMENTATION
      markov = rbind(markov,eps)
      
      if (nrow(centroids) > 1)
        markov = cbind(markov,eps)
      
      # delta representa a visita, quando um estado eh visitado
      
      # matriz de adjacencia
      #                 to
      #             [,1]      [,2]
      # from [1,]   1e-7+delta  1e-7   --> 1000/1001    1/1001 
      #      [2,]   1e-7  1e-7
      
      
     # print("centroids")
     # print(centroids)
    }
    # se nao criamos um centroide, vamos adaptar a Gaussiana visitada
    else {
      # media movel exponencialmente ponderada
      # combinacao linear simples do atual centro e do novo ponto 
      centroids[current_position,] = (1-alpha)*centroids[current_position,] + alpha*example
    }
    
    if (old_position != -1){
      # visitei alguem
      print(paste("from: ", old_position, " to: ", current_position))
      
      #markov[from, to]
      markov[old_position, current_position] = markov[old_position, current_position] + delta
    }
    
    
    # cada linha da matriz de adjacencia deve somar 1, para representar uma probabilidade a transicao 
    # para cada estado destino a partir de um esatdo origem
    for (j in 1:nrow(markov)){
      markov[j,] = markov[j,] / sum(markov[j,])
    }
    
    print('Adjacency Matrix')
    print(markov)
    
    H = entropy(markov)
    
    # atualizar a posicao, que foi transicionada 
    old_position = current_position
  }
}

X = read.table('dataset.dat')
sonde(X)





