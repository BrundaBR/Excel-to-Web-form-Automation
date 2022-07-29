# Excel-to-Web-form-Automation

## problem
The recuring process of adding data/promotion captured in file to portal either stark or sharepoint is time consuming.<br>

Current process:
Capturing promotions in excel and adding it to sharepoint portal according to specified region.

Estimated Time consumption:
Time consumed for this process is approximately 5 minutes per day and 25 minutes for a week, which is not particularly efficient.

## Solution offered
Solution i am proposing is to automate the process of manually adding data to portal such as sharepoint or stark.
Working of application:
1. Application iterates through excel ,detect region MKPL and based on MKPL navigate to url and add the corresponding data to the form.

2. After adding data, application would submit the data automatically.

End goal:
The  application will only require adding file to application and the data will automatically get stored in portal.


## Disadvantages

1. When new file is created for a region, this application would fail as new url has to be updated in backend<br>

2. The data stored in excel should be in particular format as the system decides populating data based on position of data, this would be overcome by using supreeth's excel template.

3. If there is human error in adding data in excel , application would not detect instead it would add data as it is.
