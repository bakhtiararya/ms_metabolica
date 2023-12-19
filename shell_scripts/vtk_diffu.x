cp ../images/$1_t1ca.int2 ../images/$1_t1ca.idf .

#vtkareg.x $1_fla.idf $1_adcr.idf -rigid -v 5 -dofout $1_adcr_to_fla.dof
#vtktransformation.x $1_adcr.idf $1_adcr_rigidr_fla.idf -dofin $1_adcr_to_fla.dof -target $1_fla.idf

vtkareg.x $1_t1ca.idf $1_adcr.idf -rigid -v 5 -dofout $1_adcr_rigidr_t1ca.dof
vtktransformation.x $1_adcr.idf $1_adcr_rigidr_t1ca.idf -dofin $1_adcr_rigidr_t1ca.dof -target $1_t1ca.idf
