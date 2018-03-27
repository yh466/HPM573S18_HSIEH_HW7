import scipy.stats as stat
import SurvivalClasses as SurvivalCls
import CalibrationClasses as Cls
import CalibrationSettings as CalibSets


# ----------- HW7 Problem 1 ---------- #

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

myCohort = SurvivalCls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

cohortOutcome = myCohort.simulate(TIME_STEPS)

print('Problem 1')
print('Percentage of patients survived beyond 5 years:', cohortOutcome.get_prob_five_year_survival())
print('         ')

# ----------- HW7 Problem 2 ---------- #

print('Problem 2')
print('Binomial distribution, with a parameter q representing the probability of five year survival.')
print('         ')

# ----------- HW7 Problem 3 ---------- #

# construct a binomial likelihood
weight = stat.binom.pmf(
        k=400,
        n=573,
        p=0.5,
        loc=0)

print('Problem 3')
print('The likelihood of the observed data:', weight)
print('         ')

# ----------- HW7 Problem 4 ----------- #

# create a calibration object
calibration = Cls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# estimate of annal mortality probability and the 95% credible interval
print('Problem 4')
print('Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))  # return with 4 decimals
print('         ')

# ----------- HW7 Problem 5 ----------- #

# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')

# simulate the calibrated model
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and projection interval
print('Problem 5')
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))






