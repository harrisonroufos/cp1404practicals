"""
CP1404 Practical
Project class
Estimate: 120 minutes
Actual:
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize Project instance"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """String representation of Project showing, name, start date, priority, cost estimate, completion percentage"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
