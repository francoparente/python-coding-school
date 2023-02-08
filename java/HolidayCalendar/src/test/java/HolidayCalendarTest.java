import org.junit.jupiter.api.Test;

import java.time.DayOfWeek;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

public class HolidayCalendarTest {

    @Test
    void anyDayOfWeekCanBeHoliday(){
        var aHolidayCalendar = new HolidayCalendar();
        var aSunday = LocalDate.of(2022, 11, 20);
        aHolidayCalendar.markDayOfWeekHoliday(DayOfWeek.SUNDAY);

        assertTrue(aHolidayCalendar.isHoliday(aSunday));
    }

    @Test
    void anyDateMayNotBeHoliday(){
        var aHolidayCalendar = new HolidayCalendar();
        var aMonday = LocalDate.of(2022, 11, 21);
        aHolidayCalendar.markDayOfWeekHoliday(DayOfWeek.MONDAY);

        assertTrue(aHolidayCalendar.isHoliday(aMonday));
    }

    @Test
    void lala(){
        var aHolidayCalendar = new HolidayCalendar();
        var aSaturday = LocalDate.of(2022, 11, 19);
        aHolidayCalendar.markDayOfWeekHoliday(DayOfWeek.SATURDAY);

        assertTrue(aHolidayCalendar.isHoliday(aSaturday));
    }

    @Test
    void moreThanOneDayOfWeekCanBeHoliday(){
        var aHolidayCalendar = new HolidayCalendar();
        var aSaturday = LocalDate.of(2022, 11, 19);
        var aSunday = LocalDate.of(2022, 11, 20);
        aHolidayCalendar.markDayOfWeekHoliday(DayOfWeek.SATURDAY);
        aHolidayCalendar.markDayOfWeekHoliday(DayOfWeek.SUNDAY);

        assertTrue(aHolidayCalendar.isHoliday(aSaturday));
        assertTrue(aHolidayCalendar.isHoliday(aSunday));
    }
}
