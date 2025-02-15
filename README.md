Day 1 Challenge: Menu-Based System Health Check Script

Solution-
Script Objective
We need a Bash script that:
Provides a menu for users to check disk usage, running services, memory, and CPU usage.
Sends a detailed system report via email every 4 hours.
Implements exception handling and debugging.


 Step 2: Install Required Packages
Ensure you have mailutils installed to send emails.
sudo apt update
sudo apt install mailutils -y

 Step 3: Create the Health Check Script
 nano system_health_check.sh
Now, add the following script:
#!/bin/bash
.
# Email to send reports
EMAIL="your-email@example.com"

# Function to check disk usage
check_disk_usage() {
    echo "Checking Disk Usage..."
    df -h
}

# Function to monitor running services
monitor_services() {
    echo "Monitoring Running Services..."
    systemctl list-units --type=service --state=running
}

# Function to assess memory usage
check_memory_usage() {
    echo "Checking Memory Usage..."
    free -m
}

# Function to evaluate CPU usage
check_cpu_usage() {
    echo "Checking CPU Usage..."
    mpstat 1 5
}

# Function to send a system health report
send_report() {
    REPORT="/tmp/system_health_report.txt"
    echo "Generating System Health Report..."

    echo "===== Disk Usage =====" > "$REPORT"
    df -h >> "$REPORT"
    
    echo -e "\n===== Running Services =====" >> "$REPORT"
    systemctl list-units --type=service --state=running >> "$REPORT"
    
    echo -e "\n===== Memory Usage =====" >> "$REPORT"
    free -m >> "$REPORT"
    
    echo -e "\n===== CPU Usage =====" >> "$REPORT"
    mpstat 1 5 >> "$REPORT"

    echo -e "\nSending Report to $EMAIL..."
    mail -s "System Health Report" "$EMAIL" < "$REPORT"

    echo "Report Sent Successfully!"
}

# Display Menu
while true; do
    echo "=============================="
    echo "  SYSTEM HEALTH CHECK MENU"
    echo "=============================="
    echo "1. Check Disk Usage"
    echo "2. Monitor Running Services"
    echo "3. Assess Memory Usage"
    echo "4. Evaluate CPU Usage"
    echo "5. Send System Health Report"
    echo "6. Exit"
    echo "=============================="
    read -p "Enter your choice: " choice

    case $choice in
        1) check_disk_usage ;;
        2) monitor_services ;;
        3) check_memory_usage ;;
        4) check_cpu_usage ;;
        5) send_report ;;
        6) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid choice! Please select a valid option." ;;
    esac


Step 4: Make the Script Executable
chmod +x system_health_check.sh

 Step 5: Run the Script
./system_health_check.sh
Step 6: Automate the Email Report Every Four Hours
Use cron to schedule the script to send a health report every four hours.

1️⃣ Open the crontab:
crontab -e

2️⃣ Add this line at the bottom:
0 */4 * * * /path/to/system_health_check.sh --send-report


✅ Summary
Step 1: Install mailutils & sysstat
Step 2: Create and configure the script
Step 3: Make it executable
Step 4: Run it manually
Step 5: Automate email reports using cron
🚀 Now your script will send system health reports every 4 hours! 🎉!
[Screenshot (439)](https://github.com/user-attachments/assets/c3132b6e-2f0f-461d-bcc9-3f06ded0e7a9)
![Screenshot (440)](https://github.com/user-attachments/assets/5743dac7-c398-47e1-a472-6023a49b897a)
![Screenshot (441)](https://github.com/user-attachments/assets/e095bbb5-c903-4c57-a86f-2d688f50a192)
![Screenshot (442)](https://github.com/user-attachments/assets/0c4f5a9b-8b27-4120-9325-bf95aa0363a2)
![Screenshot (439)](https://github.com/user-attachments/assets/ccdc3175-a612-400a-a9cc-eb516b792c45)



 
