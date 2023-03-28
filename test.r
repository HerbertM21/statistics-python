# Distribucion de bernoulli
bernoulli_pmf <- function(x, p) {
  return (p^x) * (1-p)^(1-x)
}

# Función de verosimilitud por producto para bernoulli
verosimilitud_bernoulli <- function(x, p) {
  v_bernoulli = 1 # Inicializar en 1
  for (i in 1:length(x)) {
    v_bernoulli = v_bernoulli * bernoulli_pmf(x[i], p)
  }
  return (v_bernoulli)
}

# Ahora utilizamos el logaritmo para rendirmiento de la verosimilitud
log_verosimilitud_bernoulli <- function(p, x) {
  return (sum(log(bernoulli_pmf(x, p))))
}

# Generar muestra aleatoria de 10 datos 0 o 1
set.seed(123) # Para reproducibilidad
x <- sample(c(0,1), size = 10, replace = TRUE)

p <- 0.5 # Valor inicial de p

# Utilizar la funcion de verosimilitud
v_bernoulli <- verosimilitud_bernoulli(x, p)
print(paste("Verosimilitud de bernoulli:", v_bernoulli))

# Utilizar la funcion de logaritmo de verosimilitud
log_v_bernoulli <- log_verosimilitud_bernoulli(p, x)
print(paste("Logaritmo de verosimilitud de bernoulli:", log_v_bernoulli))

# Maximizar la funcion de verosimilitud
library(nloptr) # Cargamos el paquete
p_opt <- nloptr(x0 = p, eval_f = function(p) -log_verosimilitud_bernoulli(p, x),
                opts = list(algorithm = "NLOPT_LN_COBYLA"))
print(paste("Valor optimo de p:", p_opt$solution))
