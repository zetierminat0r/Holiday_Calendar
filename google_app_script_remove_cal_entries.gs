/*
Search a date range in Google Calendar for events matching a given string
and then delete them.
*/


function deleteEvents() {

  // start date (MM/DD/YYYY)
  var startDate = new Date('2/26/2024');

  // end date (MM/DD/YYYY)
  var endDate = new Date('11/03/2044');

  // string to search for in the Calendar events
  var searchstring = "Holiday";

  // ID of the Calendar to access
  var calendarID = 'david.foor@zetier.com';


  // get the Calendar
  var calendar = CalendarApp.getCalendarById(calendarID);

  // create 'option' for search string
  var options = { search: searchstring };

  // get all existing events between date range, containing search string
  var existingEvents = calendar.getEvents(startDate, endDate, options);


  // count and log the number of found events
  var numEvents = existingEvents.length;
  Logger.log('Number of found events is: ' + numEvents);


  // loop through found events ***************
  for (var i = 0; i < numEvents; i++) {

    // create variable for current event
    var event = existingEvents[i];

    // get event title
    var eventTitle = event.getTitle();
    Logger.log('Event title is: ' + eventTitle);

    // delete the event
    event.deleteEvent();

  }
  // loop through found events ***************


}
