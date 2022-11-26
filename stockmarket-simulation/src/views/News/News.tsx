import * as React from 'react';
import { Col, Grid, Row } from 'react-bootstrap';
import { connect } from 'react-redux';
import { AppState, StockNews } from '../../state/AppState';
import { NewsCard } from './Cards/NewsCard';
import { getActiveNews, getInactiveNews } from '../../state/news/newsSelectors';
import { dateSortDescending } from './SortsNews';

interface NewsProps {
    activeNews: StockNews[];
    inactiveNews: StockNews[];
}

class News extends React.Component<NewsProps> {

    getActiveNewsView( activeNews: StockNews[] ) {
        return (
            <Row>
                <Col key={1} xs={12}>
                    <h3>Active News</h3>
                </Col>
                {activeNews.map( news => {
                    return (
                        <Col key={news.text} xs={12}>
                            <NewsCard news={news}/>
                        </Col>
                    );
                } )}
            </Row>
        );
    }

    getInactiveNewsView( inactiveNews: StockNews[] ) {
        return (
            <Row>
                <Col key={1} xs={12}>
                    <h3>Active News</h3>
                </Col>
                {inactiveNews.map( news => {
                    return (
                        <Col key={news.text} xs={12}>
                            <NewsCard news={news}/>
                        </Col>
                    );
                } )}
            </Row>
        );
    }

    render() {

        const {activeNews, inactiveNews} = this.props;

        return (
            <div className="content">
                <Grid fluid={true}>
                    {
                        activeNews.length > 0 &&
                        this.getActiveNewsView( activeNews )
                    }
                    <Row>
                        {
                            inactiveNews.length > 0 &&
                            this.getInactiveNewsView( inactiveNews )
                        }
                    </Row>
                </Grid>
            </div>
        );
    }
}

const mapStateToProps = ( state: AppState ) => ({
    activeNews: getActiveNews( state ),
    inactiveNews: getInactiveNews( state ).sort( dateSortDescending ),
});

// tslint:disable-next-line: no-any
const mapDispatchToProps = ( dispatch: any ) => ({});

export default connect( mapStateToProps, mapDispatchToProps )( News );
