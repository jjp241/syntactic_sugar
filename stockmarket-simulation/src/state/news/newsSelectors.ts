import { createSelector } from 'reselect';
import { AppState, StockNews } from '../AppState';

export const getNews = (state: AppState) => state.news.news;

export const getActiveNews = createSelector(
    [getNews],
    (news: StockNews[]) => {
        return news.filter(n => n.isActive);
    }
);

export const getInactiveNews = createSelector(
    [getNews],
    (news: StockNews[]) => {
        return news.filter(n => !n.isActive);
    }
);