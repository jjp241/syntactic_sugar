import * as React from 'react';
import { Card } from '../../../components/Card/Card';
import { StockNews } from '../../../state/AppState';

interface NewsCardProps {
    news: StockNews;
}

export class NewsCard extends React.Component<NewsCardProps> {

    render() {
        const { news } = this.props;

        return (
            <Card noFooter={true} noHeader={true}>
                <h4 className="title" style={{float: 'left'}}>{news.text}</h4>
            </Card>
        );
    }
}