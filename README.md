# Contact-List 📇

A simple yet effective contact management system built with Python 3. Store, organize, and manage your personal contacts right from the terminal.

## Features

- 👤 Add new contacts with detailed information
- 📋 View all contacts in a formatted list
- 📞 Store phone numbers, emails, addresses, and birthdays
- 💾 Save contacts functionality
- 🗂️ Easy-to-use menu system

## Requirements

- Python 3.x

## Installation

```bash
git clone https://github.com/Python-Swift15/Contact-List.git
cd Contact-List
```

## Usage

```bash
python3 contactlist.py
```

## How to Use

When you run the program, you'll see a menu with four options:

### Menu Options

1. **Add New Contact** - Enter contact details
2. **Display All Contacts** - View all saved contacts
3. **Save Contacts** - Save contacts to storage
4. **Exit** - Close the application

### Adding a Contact

The system will prompt you to enter:
- **Name** - Contact's full name
- **Phone** - Phone number
- **Email** - Email address
- **Birthday** - Birthday in DD/MM/YY format
- **Address** - Residential or mailing address

### Example

```
=== My Contact List ===
1. Add new contact
2. Display all contacts
3. Save contacts
4. Exit

What would you like to do? (1/2/3/4): 1

Adding new contact...
Enter name: John Doe
Enter phone: 555-1234
Enter email: john@example.com
Enter birthday (DD/MM/YY): 15/03/85
Enter address: 123 Main St, Anytown
Contact added successfully!
```

## Data Stored per Contact

Each contact record contains:
- Full Name
- Phone Number
- Email Address
- Birthday (DD/MM/YY format)
- Physical Address

## Technical Details

- Uses Python lists for data storage
- Loop-based menu system for continuous operation
- Input validation with `.strip()` method
- Indexed contact display system

## Future Enhancements

- 💾 Persistent file storage (CSV/JSON)
- 🔍 Search and filter functionality
- ✏️ Edit existing contacts
- 🗑️ Delete contact functionality
- 🔤 Sort by name, phone, or birthday
- 📱 Import/export functionality
- 🔐 Contact encryption

## Code Structure

Main components:
- Menu loop system
- Contact input handler
- Contact display formatter
- Save functionality (ready for implementation)

## License

Open source - Feel free to take inspiration!
