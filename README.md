# CSE366_genetic_algorithm


# Class Scheduling Optimization using Genetic Algorithms

This project implements a Genetic Algorithm (GA) to solve the class scheduling problem, ensuring minimal conflicts and optimal alignment with students' preferences. The program visually represents the scheduling process using Pygame.

# Table of Contents
 1. Overview
 2. Features
 3. Code Structure
 4. Genetic Algorithm Workflow
 5. Installation
 6.  Usage
 7. Visualization
 8. Future Improvements

 # Overview
 The goal of this project is to optimize class scheduling using a Genetic Algorithm. The primary objectives are:

    . Minimize Conflicts: Ensure students are not scheduled for classes during their unavailable time slots.
    . Align with Preferences: Maximize alignment between students' schedules and their preferred time slots.
    . Visualize the Process: Use Pygame to dynamically display the scheduling optimization in real time.
    . This project showcases how Genetic Algorithms can solve complex scheduling challenges while providing a clear, interactive     
       visualization of the solution's evolution.

 # Features
   1. Class Scheduling Optimization:

Classes have a duration (1–2 hours) and priority (scale of 1–5).
Students have unique availability and time slot preferences.

 2. Genetic Algorithm:

Implements selection, crossover, and mutation to evolve solutions.
Fitness function evaluates conflict minimization and preference alignment.

 3. Visualization:

Real-time schedule grid visualization using Pygame.
Highlights conflicts, class priorities, and alignment with preferences.
Displays generation count and best fitness score.

4. Configurable Parameters:

Population size, mutation rate, and number of generations can be adjusted for experimentation.


# Code Structure
     
The project is divided into three main Python classes:


1. agent.py: Defines the Student class, which includes:

     . Attributes: id, availability, preference, and schedule.

     . Methods for assigning classes based on student availability and preference, and clearing the schedule for new generations.


2. environment.py: Defines the Environment class, which:

    . Sets up the problem, including random task durations, priorities, student availability, and preferences.

    . Provides methods for generating initial schedules and drawing the task assignment grid in Pygame for visualization.


3. run.py: Contains the main script that:

    . Initializes the environment, runs the genetic algorithm, and manages the visualization of the task assignments in real-time.



# Genetic Algorithm Workflow

   The Genetic Algorithm (GA) is used to optimize class schedules in the following steps:
1. **Initial Population Creation:** A population of random schedules is generated, where each schedule is an array representing class assignments for each student.

              population = environment.generate_assignments()

             
2. **Fitness Evaluation:** Each individual in the population is evaluated using the fitness function, which considers conflicts, student preferences, and schedule balance.
            # Fitness Function (Conflict Minimization and Preference Alignment)
           def fitness(individual):
           """Calculate fitness of the schedule by minimizing conflict and preference penalties."""
                conflict_penalty = 0
              preference_penalty = 0


 #  Check each class assigned in the individual's schedule
    for class_id, student in enumerate(individual):
        slot = class_id % 24  # Assume class_id mod 24 is the slot (simplification)

           # Conflict penalty: penalize if student is unavailable at the assigned time
        if environment.student_availabilities[student, slot] == 0:
            conflict_penalty += 1


   # Preference penalty: reward the student for aligning their preferences with assigned times
        preference_penalty += abs(environment.student_preferences[student, slot] - environment.class_priorities[class_id])


 # Total fitness is the sum of conflict penalty and preference penalty
    return conflict_penalty + preference_penalty

3. **Selection:** The fittest individuals (based on the fitness function) are selected to become parents for the next generation.


     # Selection Function (Selecting the top half of the population based on fitness)
            def selection(population):
              """Selects the top half of the population based on fitness."""
             return sorted(population, key=fitness)[:population_size // 2]

        
4. **Crossover:** Parents are paired to create new offspring using single-point crossover, where the schedules of two parents are combined at a random point.

     # Crossover Function (Single-Point Crossover)

def crossover(parent1, parent2):
    """Performs single-point crossover to combine two parent schedules."""
    point = random.randint(1, num_classes - 1)
    child = np.concatenate([parent1[:point], parent2[point:]])
    return child



5. **Mutation:** Some offspring schedules are mutated by randomly reassigning classes to different students to maintain genetic diversity.


# Mutation Function 
def mutate(individual):
    """Randomly mutates the class assignments."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, num_students - 1)  # Reassign class to a random student
    return individual


6. **Next Generation:** The new offspring replace the old population, and the process continues for a defined number of generations, optimizing the schedule further.

# Crossover and mutation to create next generation
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child = crossover(parent1, parent2)
        next_generation.append(mutate(child))


    # Update population with the next generation
    population = next_generation

# Installation

###  Clone the repository:


git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
### Pygame Installation

pip install pygame
### Numpy Installation

pip install pygame numpy


# Usage
Run the main script to start the visualization:

python run.py

A Pygame window will open, displaying the task assignment grid and updates on the genetic algorithm's progress.

# Controls
Exit: Close the Pygame window by clicking the close button to exit the application.



# Visualization
The Pygame window will display the schedules in a grid format:

. Rows represent students.
. Columns represent the classes.
. Cells are color-coded based on class durations and priorities.
. Conflicts and mismatched preferences are highlighted.
. The fitness score for each generation will be displayed in the Pygame window.
. The display is updated in real-time, showing how the schedule improves with each generation.

# Future Improvements

1. Dynamic GA Parameter Adjustment: Implement dynamic adjustments to GA parameters such as mutation rate and population size based on performance.

2. Conflict and Preference Logging: Track and log the number of conflicts and preference mismatches across generations for analysis.

3. Advanced Visualization: Enhance the visualization to show more detailed information, such as conflict counts and exact preference    mismatches.

4. Student-Teacher Constraints: Add constraints to model teacher availability and class size limits.

5. Parallelization: Speed up the genetic algorithm using parallel processing to evaluate multiple populations simultaneously.






