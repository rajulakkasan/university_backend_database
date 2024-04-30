from django.core.management.base import BaseCommand
from ...models import Department, Course, Instructor, Student, Prerequisite, Section, Takes, Teaches
import os
import re

class Command(BaseCommand):
    help = 'Load data from input_data.sql into the database'

    def handle(self, *args, **options):
        file_path = '/Users/yanamalakondareddy/Clarkson/DBS/Projects/university_database_backend/data/input_data.sql'  # Path to your input_data.sql file
        with open(file_path, 'r') as f:
            sql_commands = f.read()

            # Split SQL commands by semicolon
            sql_commands = sql_commands.split(';')

            # Create a regex pattern to match table names
            table_pattern = re.compile(r'INSERT INTO `([^`]+)`')

            # Define a mapping of table names to Django models
            model_mapping = {
                'Course': Course,
                'Department': Department,
                'Instructor': Instructor,
                'Student': Student,
                'Prerequisite': Prerequisite,
                'Section': Section,
                'Takes': Takes,
                'Teaches': Teaches,
            }

            # Iterate over each SQL command and execute it
            for command in sql_commands:
                print(command)
                try:
                    # Extract table name from SQL command
                    match = table_pattern.search(command)
                    if match:
                        table_name = match.group(1)
                        # Get the corresponding Django model
                        model = model_mapping.get(table_name)
                        if model:
                            # Execute SQL command using raw SQL
                            model.objects.raw(command)
                            self.stdout.write(self.style.SUCCESS(f"Data loaded successfully for {table_name}."))
                        else:
                            self.stdout.write(self.style.ERROR(f"No model found for table {table_name}."))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error executing SQL command: {e}"))
                    continue

        self.stdout.write(self.style.SUCCESS('All data loaded successfully.'))
