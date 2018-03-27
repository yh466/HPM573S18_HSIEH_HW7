import CalibrationClassesQ6 as Cls
import CalibrationSettings as CalibSets

# ----------- HW7 Problem 6 ----------- #

# create a calibration object
calibration = Cls.Calibration()
# sample the posterior of the mortality probability
calibration.sample_posterior()

# report mean and projection interval with a larger sample size from clinical study
print('Problem 6')
print('Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))  # return with 4 decimals

# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))

print('Both the credible interval and the projection interval become narrower with larger sample size in the clinical trial.')

