import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.HashSet;
import java.util.Set;

public class HolidayCalendar {
    private Set<DayOfWeek> dayOfWeekHoliday = new HashSet<>(); //Set es una interface y HashSet es una clase que la implementa

    public Boolean isHoliday(LocalDate aDate) {
        return aDate.getDayOfWeek().equals(dayOfWeekHoliday);
    }

    public void markDayOfWeekHoliday(DayOfWeek aDayOfWeek) {
        dayOfWeekHoliday.add(aDayOfWeek);
    }
}
