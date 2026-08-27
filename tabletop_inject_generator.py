import random
import time

def generate_inject():
    """Generates a random security incident inject for tabletop exercises."""
    
    scenarios = [
        "Ransomware note discovered on the main file share.",
        "Phishing email clicked by HR director; malicious payload downloaded.",
        "DDoS attack overwhelming the customer login portal.",
        "Unauthorized login detected on CEO's Office365 account from a foreign IP.",
        "Database server CPU spiked to 100% with massive outbound traffic on port 443."
    ]
    
    systems = [
        "Internal Mail Server", 
        "HR Database", 
        "Customer Web Portal", 
        "Active Directory Domain Controller", 
        "Cloud Backup Server"
    ]
    
    print("\n" + "="*50)
    print("🚨 TABLETOP EXERCISE INJECT GENERATOR 🚨")
    print("="*50)
    print(f"Time of Inject : {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target System  : {random.choice(systems)}")
    print(f"Scenario       : {random.choice(scenarios)}")
    print("-" * 50)
    print("Action Required: Initiate NIST IR Playbook.")
    print("Determine your immediate Containment strategy.\n")

if __name__ == "__main__":
    generate_inject()
