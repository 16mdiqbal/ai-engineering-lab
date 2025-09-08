class BugTracker:

    '''A simple bug tracking system.'''
    def __init__(self):
        self.bugs = {}  # Initialize an empty dictionary to store bugs


    def add_bug(self, bug_id, description, severity, status="Open"):
        '''Adds a new bug to the tracker'''
        if bug_id in self.bugs:
            return "Bug ID already exists"
        
        else:
            self.bugs[bug_id] = {
                "description": description,
                "severity": severity,
                "status": status
            }
        print(f"Bug {bug_id} added successfully.")

    def update_status(self, bug_id, new_status):
        '''Updates the status of an existing bug.'''
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
            print(f"Bug {bug_id} status updated to {new_status}.")
        else:
            return "Bug ID not found"

    def list_all_bugs(self):
        '''Returns a list of all bugs with their details.'''
        return self.bugs        



if __name__ == "__main__":

    tracker = BugTracker()
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "Page crashes on load", "Critical")
    print(tracker.list_all_bugs())


    tracker.update_status(101, "In Progress")
    print(tracker.list_all_bugs())       

    tracker.update_status(102, "Closed")
    print(tracker.list_all_bugs())

    
    tracker.update_status(103, "Closed")  # Bug ID not found
    print(tracker.list_all_bugs())
