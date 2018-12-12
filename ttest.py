import pandas as pd 
from scipy import stats

print "Comparison between 2 groups: teacher_centered and curriculum_sequencing_adaptation"

teacher_centered_data_frame = pd.read_csv("teacher_centered.csv")
teacher_centered_ability = teacher_centered_data_frame[['ability']]
teacher_centered_final_result = teacher_centered_data_frame[['final_result']]

curriculum_sequencing_adaptation_data_frame = pd.read_csv("curriculum_sequencing_adaptation.csv")
curriculum_sequencing_adaptation_ability = curriculum_sequencing_adaptation_data_frame[['ability']]
curriculum_sequencing_adaptation_final_result = curriculum_sequencing_adaptation_data_frame[['final_result']]

print "Ability:"
print "Teacher centered: "
print(teacher_centered_ability.describe())
print "Curriculum sequencing adaptation: "
print(curriculum_sequencing_adaptation_ability.describe())

print "Final result:"
print "Teacher centered: "
print(teacher_centered_final_result.describe())
print "Curriculum sequencing adaptation: "
print(curriculum_sequencing_adaptation_final_result.describe())

print "teacher_centered mean ability: %s" % (teacher_centered_ability.mean())
print "teacher_centered mean final result: %s" % (teacher_centered_final_result.mean())

print "curriculum_sequencing_adaptation mean ability: %s" % (curriculum_sequencing_adaptation_ability.mean())
print "curriculum_sequencing_adaptation mean final result: %s" % (curriculum_sequencing_adaptation_final_result.mean())

print "Mean ability difference: %s" % (abs(teacher_centered_ability.mean() - curriculum_sequencing_adaptation_ability.mean()))
print "Mean final result difference: %s" % (abs(teacher_centered_final_result.mean() - curriculum_sequencing_adaptation_final_result.mean()))


print "T Test ability: ", stats.ttest_ind(teacher_centered_ability, curriculum_sequencing_adaptation_ability)
print "T Test ability: ", stats.ttest_ind(teacher_centered_ability, curriculum_sequencing_adaptation_ability, equal_var = False)
print "T Test final result: ", stats.ttest_ind(teacher_centered_final_result, curriculum_sequencing_adaptation_final_result)
print "T Test final result: ", stats.ttest_ind(teacher_centered_final_result, curriculum_sequencing_adaptation_final_result, equal_var = False)