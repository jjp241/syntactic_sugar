import { createSelector } from 'reselect';
import { AppState, StockNews } from '../AppState';

export const getNews = (state: AppState) => state.news.news;

export const getActiveQuests = createSelector(
    [getNews],
    (news: StockNews[]) => {
        return news.filter(n => n.isActive);
    }
);

export const getInactiveQuests = createSelector(
    [getNews],
    (news: StockNews[]) => {
        return news.filter(n => !n.isActive);
    }
);