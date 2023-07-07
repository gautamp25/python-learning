"""
    Need of condition Object:
        - To communicate with multiple threads
        - Event object: communicate between two threads

        Steps:
            - Create object of Condition class
             syntax-
                con = threading.Condition([lock_object])

        notify(): Wake up one thread
        notify_all(): Wake up multiple thread

        
"""