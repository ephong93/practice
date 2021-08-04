import React from 'react';
import { fireEvent, render } from '@testing-library/react';
import Counter from './Counter';

test('render counter', () => {
    const { getByText } = render(<Counter />);
    const titleElement = getByText(/counter/i);
    expect(titleElement).toBeInTheDocument();
});


test('check init count', () => {
    const { getByText } = render(<Counter />);

    const countElement = getByText('0');
    expect(countElement).toBeInTheDocument();

    const plusElement = getByText('+');
    expect(plusElement).toBeInTheDocument();

    const minusElement = getByText('-');
    expect(minusElement).toBeInTheDocument();


    fireEvent.click(plusElement);
    const countElement2 = getByText('1');
    expect(countElement2).toBeInTheDocument();

    fireEvent.click(minusElement);
    const countElement3 = getByText('0');
    expect(countElement3).toBeInTheDocument();
});
