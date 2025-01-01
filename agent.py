
# Agent.py
import numpy as np


class Agent:
    def __init__(self, id, availability, preferences):
        """
        Initialize the agent with an id, availability, preferences, and schedule.
        """
        self.id = id  # Unique identifier for each student
        self.availability = availability  # Availability matrix (0 = unavailable, 1 = available)
        self.preferences = preferences  # Preference for each slot (1-5 scale)
        self.schedule = []  # The schedule this agent (student) will follow


    def assign_classes(self, class_assignments):
        """
        Assign classes to this agent (student) based on availability and preferences.
        """
        self.schedule = []  # Reset schedule before assigning
        for class_id, (student, slot) in enumerate(class_assignments):
            if student == self.id and self.availability[slot] == 1:
                # Assign the class to the student if the student is available
                self.schedule.append((class_id, slot))


    def reset_schedule(self):
        """
        Clear the current schedule for the agent (student) to allow re-scheduling.
        """
        self.schedule = []  # Clear all classes from the student's schedule


    def get_fitness(self, environment):
        """
        Calculate the fitness score of the current schedule.
        Fitness is calculated based on:
        1. Number of conflicts (class in an unavailable time slot).
        2. How well the schedule aligns with the student's preferences.
        """
        conflict_penalty = 0
        preference_penalty = 0
        for class_id, slot in self.schedule:
            # Penalize if the class is scheduled when the student is unavailable
            if environment.student_availabilities[self.id, slot] == 0:
                conflict_penalty += 1


            # Penalize if the class schedule does not align with the student's preferences
            preference_penalty += abs(self.preferences[slot] - environment.class_priorities[class_id])


        # The fitness score is the sum of conflict and preference penalties
        return conflict_penalty + preference_penalty
