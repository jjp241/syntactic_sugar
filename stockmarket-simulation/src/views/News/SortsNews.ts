// This is a comparison function that will result in dates being sorted in DESCENDING order
import { StockNews } from '../../state/AppState';

export const dateSortDescending = ( news1: StockNews, news2: StockNews ) => {
    if (news1.isActive! > news2.isActive!) {
        return -1;
    } else if (news1.isActive! < news2.isActive!) {
        return 1;
    } else {
        return 0;
    }
};