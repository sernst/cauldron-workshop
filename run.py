import cauldron as cd

print('RUNNING!')

result = cd.run_project(
    project_directory='/project/workshop-example',
    output_directory='/output/display',
    logging_path='/output/run.log',
    save_to='/output/results.csv'
)

if result.success:
    print('Project ran successfully')
